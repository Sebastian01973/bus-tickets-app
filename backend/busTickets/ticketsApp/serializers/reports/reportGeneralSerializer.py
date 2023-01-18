from rest_framework import serializers

from ticketsApp.models import User
from ticketsApp.models import Client
from ticketsApp.models import BoxOffice
from ticketsApp.models import Vehicle
from ticketsApp.models import Ticket
from ticketsApp.models import Road
from ticketsApp.models import Business

from ticketsApp.serializers.ticketSerializer import TicketSerializer
from ticketsApp.serializers.vehicleSerializer import VehicleSerializer
from ticketsApp.serializers.clientSerializer import ClientSerializer
from ticketsApp.serializers.boxOfficeSerializer import BoxOfficeSerializer
from ticketsApp.serializers.userSerializer import UserSerializer
from ticketsApp.serializers.roadSerializer import RoadSerializer
from ticketsApp.serializers.businessSerializer import BusinessSerializer


class ReportGeneralSerializer(serializers.ModelSerializer):
    plate = serializers.CharField(source='vehicle.plate')

    class Meta:
        model = Ticket
        fields = ['departure_time', 'generate_date', 'quantity', 'total_value', 'plate']

    def create(self, validated_data):
        vehicleData = validated_data.pop('vehicle')
        try:
            vehicle_instance = Vehicle.objects.get(plate=vehicleData['plate'])
            reportGeneral_instance = Ticket.objects.create(vehicle=vehicle_instance, **validated_data)
            return reportGeneral_instance
        except Vehicle.DoesNotExist:
            raise serializers.ValidationError("Vehicle does not exist")
