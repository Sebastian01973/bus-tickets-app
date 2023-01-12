from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status, views, permissions, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ticketsApp.models import BoxOffice
from ticketsApp.serializers.boxOfficeSerializer import BoxOfficeSerializer


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

    serializer_class = BoxOfficeSerializer
    queryset = BoxOffice.objects.all()

    # def post(self, request, *args, **kwargs):
    #     serializer = BoxOfficeSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     token_data = {
    #         "username": request.data["username"],
    #         "password": request.data["password"]
    #     }
    #
    #     token_serializer = TokenObtainPairSerializer(data=token_data)
    #     token_serializer.is_valid(raise_exception=True)
    #
    #     return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
