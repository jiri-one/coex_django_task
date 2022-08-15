from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from swimplaces.models import SwimPlace, Category
from .serializers import SwimPlaceSerializer

@api_view(["GET"])
def get_swim_places(request):
    swimplaces = SwimPlace.objects.all()
    serializer = SwimPlaceSerializer(swimplaces, many=True)
    return Response(serializer.data)
