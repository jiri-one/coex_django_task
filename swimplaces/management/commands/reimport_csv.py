from django.core.management.base import BaseCommand, CommandError
from swimplaces.models import SwimPlace, Category
import csv
from pathlib import Path

FIELDNAMES = """
id
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
from_cr_center
""".strip().split('\n')

class Command(BaseCommand):
    help = 'Import/update new data from CSV'

    def create_swimplaces(self, SwimPlace, Category):
        with open(self.file, "r", encoding='utf-8') as file:
            reader = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=';')
            next(reader, None) # skip first line
            for row in reader:
                for key, value in dict(row).items(): 
                    if not value: # prevent empty string from csv
                        row[key] = None
                if row["category"]:
                    row["category"], _ = Category.objects.get_or_create(name=row["category"], defaults={"name": row["category"]})
                SwimPlace.objects.update_or_create(id=row["id"], defaults={**row})

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs=1, type=str)

    def handle(self, *args, **options):
        if Path(options['file_name'][0]).is_file():
            # better to handle file structure here ... but for simplicity let it this way
            self.file = options['file_name'][0]
            self.create_swimplaces(SwimPlace, Category)
            self.stdout.write(self.style.SUCCESS(f'Successfully imported file: {self.file}'))
        else:
            self.stdout.write(self.style.ERROR('You have to write correct file name.'))
