from .models import SwimPlace, Category, Comment
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .helpers import categories_count


def index(request):
    swimplaces = SwimPlace.objects.all()
    context = {'swimplaces': swimplaces}
    return render(request, 'swimplaces/index.html', context)


def stats(request):
    nr_of_swimplaces = SwimPlace.objects.count()
    categories = categories_count()
    sp_with_most_comments = Comment.objects.values("swimplace").annotate(Count('id')).order_by('-id__count')[0]["swimplace"]
    context = {'nr_of_swimplaces': nr_of_swimplaces,
               'categories': categories,
               'sp_with_most_comments': sp_with_most_comments
               }
    return render(request, 'swimplaces/stats.html', context)

# def search(request):
#     if request.method == 'POST':
#         searched_text = request.POST.get('searched_text')
#         language = request.POST.get('language')
#         fulltext = request.POST.get('optionsRadios')
#         results = db_search(language, searched_text, fulltext)
#         return HttpResponse(results)
