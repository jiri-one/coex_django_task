from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from swimplaces.models import SwimPlace, Temperature
from json import JSONDecodeError
import asyncio
import httpx
from datetime import datetime


class Command(BaseCommand):
    help = 'Asynchronously update temperature on every SwimPlaces'

    async def update_temperatures(self):
        params = {'latitude': sp.latitude,
                  'longitude': sp.longitude,
                   'current_weather': "true"}
        self.not_updated = 0
        async for sp in SwimPlace.objects.all():
            async with httpx.AsyncClient() as client:
                try:
                    resp = await client.get("https://api.open-meteo.com/v1/forecast", params=params)
                    actual_temperature = resp.json()['current_weather']['temperature']
                except (JSONDecodeError, BaseException):
                    actual_temperature = None
                    self.not_updated += 1
                if actual_temperature:
                    await Temperature.objects.aupdate_or_create(swimplace=sp, defaults={"degree": actual_temperature})
  
    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Temperature update has been started. There is lot of data to be updated, please be patient ...'))
        start_time = datetime.now()
        asyncio.run(self.update_temperatures())
        time = datetime.now() - start_time
        cache.clear() # delete old cache
        self.stdout.write(self.style.SUCCESS(f'Successfully have been writen/updated temperatures and it takes {time.seconds//60} minutes and {time.seconds%60} seconds.'))
        if self.not_updated > 0:
            self.stdout.write(self.style.NOTICE(f'And {self.not_updated} temperatures were not updated.'))
