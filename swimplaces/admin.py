from django.contrib import admin

from .models import *

for model in (SwimPlace, Category, Comment, Temperature):
    admin.site.register(model)
