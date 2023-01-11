from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.boxOffice import BoxOffice
from ticketsApp.serializers.boxOfficeSerializer import BoxOfficeSerializer


@extend_schema_view(
    list=extend_schema(description="List all box offices"),
    retrieve=extend_schema(description="Retrieve a box office"),
    create=extend_schema(description="Create a box office"),
    update=extend_schema(description="Update a box office"),
    destroy=extend_schema(description="Delete a box office")
)
class BoxOfficeViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = BoxOffice.objects.all()
    serializer_class = BoxOfficeSerializer
