from ticketsApp.models.road import Road
from rest_framework import serializers


class RoadSerializer(serializers.ModelSerializer):
    """Serializer for RoadSerializer Model Class"""
    class Meta:
        model = Road
        fields = '__all__'
