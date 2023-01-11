from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.role import Role
from ticketsApp.serializers.roleSerializer import RoleSerializer


@extend_schema_view(
    list=extend_schema(description="List all roles"),
    retrieve=extend_schema(description="Retrieve a role"),
    create=extend_schema(description="Create a role"),
    update=extend_schema(description="Update a role"),
    destroy=extend_schema(description="Delete a role")
)
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

