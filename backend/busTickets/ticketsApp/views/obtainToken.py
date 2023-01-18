from rest_framework_simplejwt.views import TokenObtainPairView

from ticketsApp.serializers.jwtSerializer import JWTSerializer


class ObtainTokenView(TokenObtainPairView):
    serializer_class = JWTSerializer

