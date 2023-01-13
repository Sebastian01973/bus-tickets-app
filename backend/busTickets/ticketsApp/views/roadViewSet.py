from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.road import Road
from ticketsApp.serializers.roadSerializer import RoadSerializer


@extend_schema_view(
    list=extend_schema(description="List all roads"),
    retrieve=extend_schema(description="Retrieve a road"),
    update=extend_schema(description="Update a road"),
    destroy=extend_schema(description="Delete a road")
)
class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer
