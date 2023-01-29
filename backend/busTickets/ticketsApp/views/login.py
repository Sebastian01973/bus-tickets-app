from rest_framework_simplejwt.views import TokenObtainPairView

from ticketsApp.serializers.jwtserializer import JwtSerializer


class Login(TokenObtainPairView):
    serializer_class = JwtSerializer
