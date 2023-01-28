from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.business import Business
from ticketsApp.serializers.businessSerializer import BusinessSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all businesses",
        description="Return a list of all the businesses"),
    retrieve=extend_schema(
        summary="Retrieve a business",
        description="Get details about a specific business"),
    create=extend_schema(
        summary="Create a business",
        description="Return details about a newly created business"),
    update=extend_schema(
        summary="Update a business",
        description="Return details about an updated business"),
    destroy=extend_schema(
        summary="Delete a business",
        description="Delete a business and return status code 204"),
)
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
