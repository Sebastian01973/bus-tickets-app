from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models import Ticket
from ticketsApp.serializers.ticketSerializer import TicketSerializer


@extend_schema_view(
    list=extend_schema("List all tickets"),
    create=extend_schema("Create a new ticket"),
    retrieve=extend_schema("Retrieve a ticket"),
    update=extend_schema("Update a ticket"),
    destroy=extend_schema("Delete a ticket"),
)
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
