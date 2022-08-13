from .models import SwimPlace, Category
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    swimplaces = SwimPlace.objects.all()
    context = {'swimplaces': swimplaces}
    return render(request, 'swimplaces/index.html', context)

# def search(request):
#     if request.method == 'POST':
#         searched_text = request.POST.get('searched_text')
#         language = request.POST.get('language')
#         fulltext = request.POST.get('optionsRadios')
#         results = db_search(language, searched_text, fulltext)
#         return HttpResponse(results)
