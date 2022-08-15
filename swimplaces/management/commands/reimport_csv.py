from django.core.management.base import BaseCommand, CommandError
from swimplaces.models import SwimPlace, Category
import csv
from pathlib import Path

FIELDNAMES = """
mapotic_id
longitude
latitude
name
category
rating
image_url
import_id
description1
address
web
e_mail
phone_number
description2
refreshment
diving
entrance
parking
link
nudist_beach
video
dog_swimming
""".strip().split('\n')

class Command(BaseCommand):
    help = 'Delete whole DB and import new data from CSV'
    
    def create_categories(self, Category):
        with open(self.file, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=';')
            next(reader, None) # skip first line
            for row in reader:
                if row["category"]: # prevent empty category
                    try:
                        category = Category.objects.get(name=row["category"])
                    except Category.DoesNotExist:
                        category = Category(name=row["category"])
                        category.save()

    def create_swimplaces(self, SwimPlace, Category):
        with open(self.file, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=';')
            next(reader, None) # skip first line
            for row in reader:
                for key, value in dict(row).items(): # prevent empty string from csv
                    if not value:
                        row[key] = None
                if row["category"]:
                    row["category"] = Category.objects.get(name=row["category"])
                swimplace = SwimPlace(**row)
                swimplace.save()

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs=1, type=str)

    def handle(self, *args, **options):
        if Path(options['file_name'][0]).is_file():
            # better to handle here file structure ... but for simplicity let it this way
            self.file = options['file_name'][0]
            # clean all previous imports
            SwimPlace.objects.all().delete()
            Category.objects.all().delete()
            # and then import all
            self.create_categories(Category)
            self.create_swimplaces(SwimPlace, Category)
            self.stdout.write(self.style.SUCCESS(f'Successfully imported file: {self.file}'))
        else:
            self.stdout.write(self.style.ERROR('You have to write correct file name.'))
