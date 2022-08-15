from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_swimplaces, name='index'),
    path('swimplace/<int:id>/', views.get_one_swimplace, name='swimplace'),
    # path('eng', views.index_eng, name='index_eng'),
    # path('search', views.search, name='search'),
]
