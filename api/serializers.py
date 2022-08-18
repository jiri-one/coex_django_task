from rest_framework import serializers
from swimplaces.models import SwimPlace, Temperature

# another solution for nested temperature field
class TemperatureField(serializers.RelatedField):
    def to_representation(self, instance):
        return instance.degree, instance.update_time

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['degree', 'update_time']

class SwimPlacesSerializer(serializers.ModelSerializer):
    temperature = TemperatureSerializer(many=True, read_only=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = SwimPlace
        fields = ["id", "name", "category", "dog_swimming", "temperature"]

class OneSwimPlaceSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = SwimPlace
        fields = "__all__"
