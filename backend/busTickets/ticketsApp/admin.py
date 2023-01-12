from django.contrib import admin

from ticketsApp.models import MyUser
from ticketsApp.models.user import User
from ticketsApp.models.role import Role

admin.site.register(Role)
admin.site.register(User)
admin.site.register(MyUser)
