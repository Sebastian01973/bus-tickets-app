from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from ticketsApp.models import BoxOffice
from ticketsApp.serializers.boxOfficeSerializer import BoxOfficeSerializer
from rest_framework.response import Response


@extend_schema_view(
    list=extend_schema(description="List all users"),
    retrieve=extend_schema(description="Retrieve a user"),
    create=extend_schema(description="Create a user"),
    update=extend_schema(description="Update a user"),
    destroy=extend_schema(description="Delete a user"),
)
class BoxOfficeCreateView(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def post(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

    @action(detail=True, methods=['get'])
    def set_password(self, request, pk=None):
        pass

    serializer_class = BoxOfficeSerializer
    queryset = BoxOffice.objects.all()
