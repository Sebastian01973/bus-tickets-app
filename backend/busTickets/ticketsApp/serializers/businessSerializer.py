from rest_framework import serializers

from ticketsApp.models.business import Business


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
