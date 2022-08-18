from django.core.management.base import BaseCommand, CommandError
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
        except JSONDecodeError:
            return None
        return meteo['current_weather']['temperature']
  
    def handle(self, *args, **options):
        Temperature.objects.all().delete()
        for sp in SwimPlace.objects.all():
            actual_temperature = self.return_temperature(sp.latitude, sp.longitude)
            temperature = Temperature(degree=actual_temperature, swimplace=sp)
            temperature.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully have been writen temperatures'))
