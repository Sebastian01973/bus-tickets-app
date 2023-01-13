from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.business import Business
from ticketsApp.serializers.businessSerializer import BusinessSerializer


@extend_schema_view(
    list=extend_schema(description="List all businesses"),
    retrieve=extend_schema(description="Retrieve a business"),
    create=extend_schema(description="Create a business"),
    update=extend_schema(description="Update a business"),
    destroy=extend_schema(description="Delete a business")
)
class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
