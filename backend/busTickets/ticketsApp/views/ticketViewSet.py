from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models import Ticket
from ticketsApp.serializers.ticketSerializer import TicketSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all tickets",
        description="Return a list of all the tickets"),
    retrieve=extend_schema(
        summary="Retrieve a ticket",
        description="Get details about a specific ticket"),
    create=extend_schema(
        summary="Create a ticket",
        description="Return details about a newly created ticket"),
    update=extend_schema(
        summary="Update a ticket",
        description="Return details about an updated ticket"),
    destroy=extend_schema(
        summary="Delete a ticket",
        description="Delete a ticket and return status code 204"),
)
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
