from rest_framework import serializers

from ticketsApp.models.role import Role


class RoleSerializer(serializers.ModelSerializer):
    """Serializer for Role Model Class"""
    class Meta:
        model = Role
        fields = '__all__'
