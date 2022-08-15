from rest_framework import serializers
from swimplaces.models import SwimPlace, Category

class SwimPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimPlace
        fields = ["id", "name"]
        # fields = "__all__"
