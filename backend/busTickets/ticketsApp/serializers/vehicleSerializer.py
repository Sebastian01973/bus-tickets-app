from rest_framework import serializers

from ticketsApp.models.vehicle import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
