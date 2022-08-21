from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from swimplaces.models import SwimPlace, Temperature
from openmeteo_py import Options, OWmanager
from json import JSONDecodeError
from datetime import datetime


class Command(BaseCommand):
    help = 'Update temperature on every SwimPlaces'

    def return_temperature(self, latitude, longitude):
        options = Options(latitude,longitude,current_weather=True)
        mgr = OWmanager(options)
        self.not_updated = 0
        try:
            meteo = mgr.get_data()
        except (JSONDecodeError, BaseException):
            self.not_updated += 1
            return None
        return meteo['current_weather']['temperature']
  
    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Temperature update has been started. There is lot of data to be updated, please be patient ...'))
        start_time = datetime.now()
        for sp in SwimPlace.objects.all():
            actual_temperature = self.return_temperature(sp.latitude, sp.longitude)
            if actual_temperature:
                Temperature.objects.update_or_create(swimplace=sp, defaults={ "degree": actual_temperature})
        time = datetime.now() - start_time
        cache.clear() # delete old cache
        self.stdout.write(self.style.SUCCESS(f'Successfully have been writen/updated temperatures and it takes {time.seconds//60} minutes and {time.seconds%60} seconds.'))
        if self.not_updated > 0:
            self.stdout.write(self.style.NOTICE(f'And {self.not_updated} temperatures were not updated.'))
