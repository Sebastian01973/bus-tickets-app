from django.contrib.auth import user_logged_out, authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ticketsApp.serializers.logoutSerializer import LogoutSerializer


class LogOut(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, req):
        try:
            serializer = self.serializer_class(data=req.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            try:
                user = authenticate(username=req.data['username'], password=req.data['password'])
                user_logged_out.send(sender=user.__class__, username=user.username, request=req, )
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response({'message: ', e}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
