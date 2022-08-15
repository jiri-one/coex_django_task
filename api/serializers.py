from rest_framework import serializers
from swimplaces.models import SwimPlace

class SwimPlacesSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = SwimPlace
        fields = ["id", "name", "category", "dog_swimming"]

class OneSwimPlaceSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = SwimPlace
        fields = "__all__"
