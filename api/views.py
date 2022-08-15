from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from swimplaces.models import SwimPlace, Category
from .serializers import SwimPlacesSerializer, OneSwimPlaceSerializer

@api_view(["GET"])
def get_swimplaces(request):
    swimplaces = SwimPlace.objects.all()
    serializer = SwimPlacesSerializer(swimplaces, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def get_one_swimplace(request, id):
    swimplace = SwimPlace.objects.filter(id=id)
    serializer = OneSwimPlaceSerializer(swimplace, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_swim_place_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
