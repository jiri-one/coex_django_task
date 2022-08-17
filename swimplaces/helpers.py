from .models import SwimPlace, Category

def categories_count():
    categories = {}
    for category in Category.objects.all():
        categories[category.name] = SwimPlace.objects.filter(category=category).count()
    return categories
