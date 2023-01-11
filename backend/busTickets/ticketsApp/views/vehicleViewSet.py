from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from ticketsApp.models.vehicle import Vehicle
from ticketsApp.serializers.vehicleSerializer import VehicleSerializer


@extend_schema_view(
    list=extend_schema(description="List all vehicles"),
    retrieve=extend_schema(description="Retrieve a vehicle"),
    create=extend_schema(description="Create a vehicle"),
    update=extend_schema(description="Update a vehicle"),
    destroy=extend_schema(description="Delete a vehicle")
)
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
