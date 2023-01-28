from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from ticketsApp.models import BoxOffice
from ticketsApp.serializers.boxOfficeSerializer import BoxOfficeSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all box offices",
        description="Return a list of all the box offices"),
    retrieve=extend_schema(
        summary="Retrieve a box office",
        description="Get details about a specific box office"),
    create=extend_schema(
        summary="Create a box office",
        description="Return details about a newly created box office"),
    update=extend_schema(
        summary="Update a box office",
        description="Return details about an updated box office"),
    destroy=extend_schema(
        summary="Delete a box office",
        description="Delete a box office and return status code 204"),
)
class BoxOfficeCreateView(viewsets.ModelViewSet):
    serializer_class = BoxOfficeSerializer
    queryset = BoxOffice.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


