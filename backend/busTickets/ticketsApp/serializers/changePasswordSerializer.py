from django.contrib.auth import password_validation
from rest_framework import serializers

from ticketsApp.models import BoxOffice


class ChangePasswordSerializer(serializers.Serializer):
    pass
    # model = BoxOffice
    #
    # old_password = serializers.CharField(required=True)
    # new_password = serializers.CharField(required=True)

    # old_password = serializers.CharField(required=True, max_length=256, write_only=True)
    # new_password = serializers.CharField(required=True, max_length=256, write_only=True)
    # confirm_new_password = serializers.CharField(required=True, max_length=256, write_only=True)
    #
    # def validate_old_password(self, value):
    #     if not self.instance.check_password(value):
    #         raise serializers.ValidationError("Old password is not correct")
    #     return value
    #
    # def validate(self, data):
    #     if data['new_password'] != data['confirm_new_password']:
    #         raise serializers.ValidationError("New password and confirm new password do not match")
    #     password_validation.validate_password(data['new_password'], self.context['request'].BoxOffice)
    #     return data
    #
    # def save(self, **kwargs):
    #     password = self.validated_data['new_password']
    #     BoxOffice = self.context['request'].BoxOffice
    #     BoxOffice.set_password(password)
    #     BoxOffice.save()
    #     return BoxOffice
