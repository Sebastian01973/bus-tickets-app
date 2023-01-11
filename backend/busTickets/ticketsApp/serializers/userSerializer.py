from rest_framework import serializers

from ticketsApp.models.user import User
from ticketsApp.models.role import Role


class UserSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = User
        fields = '__all__'


