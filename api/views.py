from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from swimplaces.models import SwimPlace, Category, Comment
from .serializers import SwimPlacesSerializer, OneSwimPlaceSerializer

@api_view(["GET"])
def get_swimplaces(request):
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
