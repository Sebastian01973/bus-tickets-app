from django.contrib.auth import authenticate, user_logged_in
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


def authenticate_user(username, password, request):
    user = authenticate(email=username, password=password, request=request)
    return user


class JwtSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        if all(credentials.values()):
            user = authenticate(request=self.context['request'], **credentials)
            if user:
                payload = self.get_token(user)
                user_logged_in.send(sender=user.__class__, request=self.context['request'], user=user)
                return {
                    'access': str(payload.access_token),
                    'refresh': str(payload),
                }
            else:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "{username_field}" and "password".'
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)
