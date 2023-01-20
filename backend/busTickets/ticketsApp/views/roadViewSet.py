from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.road import Road
from ticketsApp.serializers.roadSerializer import RoadSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all roads",
        description="Return a list of all the roads"),
    retrieve=extend_schema(
        summary="Retrieve a road",
        description="Get details about a specific road"),
    create=extend_schema(
        summary="Create a road",
        description="Return details about a newly created road"),
    update=extend_schema(
        summary="Update a road",
        description="Return details about an updated road"),
    destroy=extend_schema(
        summary="Delete a road",
        description="Delete a road and return status code 204"),
)
class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer
