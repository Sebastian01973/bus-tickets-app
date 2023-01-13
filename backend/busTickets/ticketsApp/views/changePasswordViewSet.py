from rest_framework import viewsets, status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token

from ticketsApp.models import boxOffice
from ticketsApp.serializers.changePasswordSerializer import ChangePasswordSerializer


class ChangePasswordViewSet(UpdateAPIView):
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.boxOffice

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if hasattr(boxOffice, 'auth_token'):
            boxOffice.auth_token.delete()
        token, created = Token.objects.get_or_create(boxOffice=boxOffice)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
