from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import viewsets

from ticketsApp.models.role import Role
from ticketsApp.serializers.roleSerializer import RoleSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all roles",
        description="Return a list of all the roles"),
    retrieve=extend_schema(
        summary="Retrieve a role",
        description="Get details about a specific role"),
    create=extend_schema(
        summary="Create a role",
        description="Return details about a newly created role"),
    update=extend_schema(
        summary="Update a role",
        description="Return details about an updated role"),
    destroy=extend_schema(
        summary="Delete a role",
        description="Delete a role and return status code 204"),
)
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

