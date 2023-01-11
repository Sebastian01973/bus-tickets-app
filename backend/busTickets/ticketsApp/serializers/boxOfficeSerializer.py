from rest_framework import serializers

from ticketsApp.models.boxOffice import BoxOffice


class BoxOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOffice
        fields = '__all__'
