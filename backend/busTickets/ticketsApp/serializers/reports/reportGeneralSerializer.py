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
    plate = VehicleSerializer()
    name = BusinessSerializer()
    user = UserSerializer()
    road = RoadSerializer()
    box_office = BoxOfficeSerializer()
    client = ClientSerializer()
    ticket = TicketSerializer()

    class Meta:
        model = Ticket, Vehicle, Business, Road, Client, User, BoxOffice
        fields = Vehicle.plate, Business.name, User.name, User.last_name, Road.destiny, Ticket.total_value,\
            Ticket.departure_time, Ticket.generate_date, Ticket.quantity
