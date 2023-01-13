from rest_framework import serializers

from ticketsApp.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client Model Class"""
    class Meta:
        model = Client
        fields = '__all__'
