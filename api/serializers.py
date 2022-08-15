from rest_framework import serializers
from swimplaces.models import SwimPlace, Category

class SwimPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimPlace
        fields = ["id", "name"]

class OneSwimPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimPlace
        fields = "__all__"
