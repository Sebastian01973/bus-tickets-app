from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from ticketsApp.models.annulation import Annulation
from ticketsApp.serializers.annulationSerializer import AnnulationSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all annulations",
        description="Return a list of all the annulations"),
    retrieve=extend_schema(
        summary="Retrieve an annulation",
        description="Get details about a specific annulation"),
    create=extend_schema(
        summary="Create an annulation",
        description="Return details about a newly created annulation"),
    update=extend_schema(
        summary="Update an annulation",
        description="Return details about an updated annulation"),
    destroy=extend_schema(
        summary="Delete an annulation",
        description="Delete an annulation and return status code 204"),
)
class AnnulationViewSet(viewsets.ModelViewSet):
    queryset = Annulation.objects.all()
    serializer_class = AnnulationSerializer
