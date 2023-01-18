from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from ticketsApp.models.annulation import Annulation
from ticketsApp.serializers.annulationSerializer import AnnulationSerializer


@extend_schema_view(
    list=extend_schema(description="List all users"),
    retrieve=extend_schema(description="Retrieve a BoxOffice"),
    create=extend_schema(description="Create a BoxOffice"),
    update=extend_schema(description="Update a BoxOffice"),
    destroy=extend_schema(description="Delete a BoxOffice"),
)
class AnnulationViewSet(viewsets.ModelViewSet):
    queryset = Annulation.objects.all()
    serializer_class = AnnulationSerializer
