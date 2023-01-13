from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.client import Client
from ticketsApp.serializers.clientSerializer import ClientSerializer


@extend_schema_view(
    list=extend_schema(description="List all clients"),
    retrieve=extend_schema(description="Retrieve a client"),
    create=extend_schema(description="Create a cllient"),
    update=extend_schema(description="Update a client"),
    destroy=extend_schema(description="Delete a client")
)
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
