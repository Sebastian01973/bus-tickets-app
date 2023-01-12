from rest_framework import serializers

from ticketsApp.models.myUser import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
