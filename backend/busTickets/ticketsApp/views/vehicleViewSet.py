from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from ticketsApp.models.vehicle import Vehicle
from ticketsApp.serializers.vehicleSerializer import VehicleSerializer



@extend_schema_view(
    list=extend_schema(
        summary="List all vehicles",
        description="Return a list of all the vehicles"),
    retrieve=extend_schema(
        summary="Retrieve a vehicle",
        description="Get details about a specific vehicle"),
    create=extend_schema(
        summary="Create a vehicle",
        description="Return details about a newly created vehicle"),
    update=extend_schema(
        summary="Update a vehicle",
        description="Return details about an updated vehicle"),
    destroy=extend_schema(
        summary="Delete a vehicle",
        description="Delete a vehicle and return status code 204"),
)
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
