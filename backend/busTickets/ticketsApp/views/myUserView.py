from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, permissions

from ticketsApp.models.myUser import MyUser
from ticketsApp.serializers.myUserSerializer import MyUserSerializer


@extend_schema_view(
    list=extend_schema(description="List all users"),
    retrieve=extend_schema(description="Retrieve a user"),
    create=extend_schema(description="Create a user"),
    update=extend_schema(description="Update a user"),
    destroy=extend_schema(description="Delete a user"),
)
class MyUserViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()
