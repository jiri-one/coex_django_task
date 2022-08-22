from django.core.management.base import BaseCommand, CommandError
from swimplaces.models import SwimPlace, Category
import csv
from pathlib import Path
from datetime import datetime
import asyncio
from aiofile import async_open
from aiocsv import AsyncDictReader

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
    
    async def create_one_swimplace(self, row):
        for key, value in dict(row).items(): 
            if not value: # prevent empty string from csv
                row[key] = None
        if row["category"]:
            row["category"], _ = await Category.objects.aget_or_create(name=row["category"], defaults={"name": row["category"]})
        await SwimPlace.objects.aupdate_or_create(id=row["id"], defaults={**row})

    async def create_swimplaces(self, SwimPlace, Category):
        async with async_open(self.file, "r", encoding='utf-8') as afile:
            areader = AsyncDictReader(afile, fieldnames=FIELDNAMES, delimiter=';')
            await areader.__anext__() # skip first line
            tasks = []
            async for row in areader:
                tasks.append(asyncio.create_task(self.create_one_swimplace(row)))

            await asyncio.gather(*tasks)

    def add_arguments(self, parser):
        parser.add_argument('file_name', nargs=1, type=str)

    def handle(self, *args, **options):
        if Path(options['file_name'][0]).is_file():
            # better to handle file structure here ... but for simplicity let it this way
            self.file = options['file_name'][0]
            start_time = datetime.now()
            asyncio.run(self.create_swimplaces(SwimPlace, Category))
            time = datetime.now() - start_time
            self.stdout.write(self.style.SUCCESS(f'Successfully imported file: {self.file} and it takes {time.seconds//60} minutes and {time.seconds%60} seconds.'))
        else:
            self.stdout.write(self.style.ERROR('You have to write correct file name.'))
