from rest_framework import serializers

from ticketsApp.models.annulation import Annulation


class AnnulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annulation
        fields = '__all__'
