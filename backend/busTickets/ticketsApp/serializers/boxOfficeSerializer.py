from rest_framework import serializers

from ticketsApp.models import BoxOffice


class BoxOfficeSerializer(serializers.ModelSerializer):
    """Serializer for BoxOffice Model Class"""
    class Meta:
        model = BoxOffice
        fields = '__all__'
