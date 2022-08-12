from sys import path as sys_path
from pathlib import Path
from contextlib import contextmanager
from os import environ
import csv

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


def create_categories(Category):
    with open("swimplaces_export.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=FIELDNAMES, delimiter=';')
        next(reader, None) # skip first line
        for row in reader:
            if row["category"]: # prevent empty category
                try:
                    category = Category.objects.get(name=row["category"])
                except Category.DoesNotExist:
                    category = Category(name=row["category"])
                    category.save()

def create_swimplaces(SwimPlace, Category):
    with open("swimplaces_export.csv", "r") as file:
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

with django_context():
    from swimplaces.models import SwimPlace, Category
    # clean all previous imports
    SwimPlace.objects.all().delete()
    Category.objects.all().delete()
    # and then import all
    create_categories(Category)
    create_swimplaces(SwimPlace, Category)
