from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from swimplaces.models import SwimPlace, Temperature
from openmeteo_py import Options, OWmanager
from json import JSONDecodeError


class Command(BaseCommand):
    help = 'Update temperature on every SwimPlaces'

    def return_temperature(self, latitude, longitude):
        options = Options(latitude,longitude,current_weather=True)
        mgr = OWmanager(options)
        try:
            meteo = mgr.get_data()
        except (JSONDecodeError, BaseException):
            return None
        return meteo['current_weather']['temperature']
  
    def handle(self, *args, **options):
        for sp in SwimPlace.objects.all():
            actual_temperature = self.return_temperature(sp.latitude, sp.longitude)
            if actual_temperature:
                Temperature.objects.update_or_create(swimplace=sp, defaults={ "degree": actual_temperature})
        cache.clear() # refresh cache
        self.stdout.write(self.style.SUCCESS(f'Successfully have been writen/updated temperatures'))
