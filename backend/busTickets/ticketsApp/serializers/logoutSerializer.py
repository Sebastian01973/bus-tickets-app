from django.contrib.auth import user_logged_out
from rest_framework import serializers
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class LogoutSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    refresh = serializers.CharField()
    # username = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        print(self.context)
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
            # print(self.context)
            # user_logged_out.send(sender=self.__class__, request=self.context['request'], user=self.user)
        except TokenError:
            self.fail('bad_token')
