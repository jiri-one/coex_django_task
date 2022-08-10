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
"""

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

with django_context():
    from swimplaces.models import SwimPlace, Category
    fieldnames = FIELDNAMES.strip().split('\n')
    categories_dictcreate_categories()
    with open("swimplaces_export.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=';')
        next(reader, None) # skip first line
        for row in reader:
            dict_row = create_(line.decode())
            # record = SwimPlace(**dict_row)
            # record.save()
