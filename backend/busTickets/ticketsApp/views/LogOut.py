from datetime import datetime
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from ticketsApp.models import BoxOffice


class LogOut(GenericAPIView):

    def post(self, request, *args, **kwargs):
        user = BoxOffice.objects.filter(id=request.data.get('id', 0))
        print("Entro a LogOut")
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
