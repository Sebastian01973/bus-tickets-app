from rest_framework import serializers

from ticketsApp.models.vehicle import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """Serializer for Vehicle Model Class"""
    class Meta:
        model = Vehicle
        fields = '__all__'
