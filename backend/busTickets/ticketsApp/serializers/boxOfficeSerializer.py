from rest_framework import serializers

from ticketsApp.models import MyUser, BoxOffice
from ticketsApp.models.user import User
from ticketsApp.serializers.userSerializer import UserSerializer


# class BoxOfficeSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#
#     class Meta:
#         model = MyUser
#         fields = '__all__'
#
#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#
#         try:
#             user_instance = User.objects.get(name=user_data.get(''))
#         except Exception as _:
#             user_instance = User.objects.create(**user_data)
#
#         box_office_instance = BoxOffice.objects.create(user=user_instance, **validated_data)
#         return box_office_instance
#
#     def to_representation(self, obj):
#         if hasattr(obj, 'id'):
#             return BoxOfficeSerializer.create_dict(obj)
#         else:
#             datas = {}
#             for p in obj:
#                 datas['box_office' + str(p.id)] = BoxOfficeSerializer.create_dict(p)
#             return datas
#
#     def create_dict(obj):
#         box_office = BoxOffice.objects.get(id=obj.id)
#         user = User.objects.get(id=box_office.id_user)
#         return {
#             'id': box_office.id,
#             'username': box_office.username,
#             'address': box_office.address,
#             'email': box_office.email,
#             'user': {
#                 'id_user': user.id,
#                 'name': user.name,
#                 'last_name': user.last_name,
#             }
#         }


class BoxOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOffice
        fields = '__all__'
