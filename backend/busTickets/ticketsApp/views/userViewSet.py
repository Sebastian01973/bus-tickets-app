from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.user import User
from ticketsApp.serializers.userSerializer import UserSerializer


@extend_schema_view(
    list=extend_schema(description="List all users"),
    retrieve=extend_schema(description="Retrieve a user"),
    create=extend_schema(description="Create a user"),
    update=extend_schema(description="Update a user"),
    destroy=extend_schema(description="Delete a user")
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
