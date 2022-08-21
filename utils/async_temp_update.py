from sys import path as sys_path
from pathlib import Path
from contextlib import contextmanager
from os import environ
import asyncio
import httpx
from django.core.cache import cache
from json import JSONDecodeError

@contextmanager
def django_context():
    try:
        django_dir = str(Path(__file__).parent.parent)
        sys_path.append(django_dir)
        from django.core.wsgi import get_wsgi_application
        environ["DJANGO_SETTINGS_MODULE"] = "coex_django_task.settings"
        application = get_wsgi_application()
        yield
    finally:
        sys_path.remove(django_dir)
        del application

async def update_temperatures(SwimPlace, Temperature):
    async for sp in SwimPlace.objects.all():
        params = {'latitude': sp.latitude,
                  'longitude': sp.longitude,
                  'current_weather': "true"}
        async with httpx.AsyncClient() as client:
            try:
                resp = await client.get("https://api.open-meteo.com/v1/forecast", params=params)
                actual_temperature = resp.json()['current_weather']['temperature']
            except (JSONDecodeError, BaseException):
                actual_temperature = None
            if actual_temperature:
                await Temperature.objects.aupdate_or_create(swimplace=sp, defaults={"degree": actual_temperature})
    
async def main():
    with django_context():
        from swimplaces.models import SwimPlace, Temperature
        await update_temperatures(SwimPlace, Temperature)
        cache.clear()
    
asyncio.run(main())
