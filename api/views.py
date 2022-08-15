from unicodedata import category
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from swimplaces.models import SwimPlace, Category, Comment
from .serializers import SwimPlacesSerializer, OneSwimPlaceSerializer

@api_view(["GET", "POST"])
def get_swimplaces(request):
    if request.method == "POST":
        # create filter in json: {"category": "Sea", "dog_swimming": "Suitable for dogs"} or combination
        search_dict = dict(request.data)
        if "category" in search_dict.keys():
            category = Category.objects.get(name=search_dict["category"])
            search_dict["category"] = category
        swimplaces = SwimPlace.objects.filter(**search_dict)
        serializer = SwimPlacesSerializer(swimplaces, many=True)
        return Response(serializer.data)
    elif request.method == "GET":
        swimplaces = SwimPlace.objects.all()
        serializer = SwimPlacesSerializer(swimplaces, many=True)
        return Response(serializer.data)

@api_view(["GET", "POST"])
def get_one_swimplace(request, id):
    if request.method == "POST":
        swimplace = SwimPlace.objects.get(id=id)
        # add comment in json form like {"comment": "your comment of place"}
        comment = Comment(text=request.data["comment"], swimplace=swimplace)
        comment.save()
        serializer = OneSwimPlaceSerializer(swimplace)
        return Response(serializer.data)
    elif request.method == "GET":
        swimplace = SwimPlace.objects.get(id=id)
        serializer = OneSwimPlaceSerializer(swimplace)
        return Response(serializer.data)

# another solution, maybe in next version
# @api_view(["POST"])
# def add_swim_place_comment(request):
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
