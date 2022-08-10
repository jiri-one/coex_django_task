from django.contrib import admin

from .models import *

for model in (SwimPlace, Category):
    admin.site.register(model)
