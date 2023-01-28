from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from ticketsApp.models.user import User
from ticketsApp.serializers.userSerializer import UserSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List all users",
        description="Return a list of all the users"),
    retrieve=extend_schema(
        summary="Retrieve an user",
        description="Get details about a specific user"),
    create=extend_schema(
        summary="Create an user",
        description="Return details about a newly created user"),
    update=extend_schema(
        summary="Update an user",
        description="Return details about an updated user"),
    destroy=extend_schema(
        summary="Delete an user",
        description="Delete an user and return status code 204"),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
