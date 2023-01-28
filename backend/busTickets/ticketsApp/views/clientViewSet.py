from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.client import Client
from ticketsApp.serializers.clientSerializer import ClientSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all clients",
        description="Return a list of all the clients"),
    retrieve=extend_schema(
        summary="Retrieve a client",
        description="Get details about a specific client"),
    create=extend_schema(
        summary="Create a client",
        description="Return details about a newly created client"),
    update=extend_schema(
        summary="Update a client",
        description="Return details about an updated client"),
    destroy=extend_schema(
        summary="Delete a client",
        description="Delete a client and return status code 204"),
)
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
