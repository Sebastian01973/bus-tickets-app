from rest_framework import serializers

from ticketsApp.models.role import Role


class RoleSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Role
        fields = '__all__'
