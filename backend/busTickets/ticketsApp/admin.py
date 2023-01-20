from django.contrib import admin

from ticketsApp.models.activity.UserLoginActivity import UserLoginActivity
from ticketsApp.models.user import User
from ticketsApp.models.role import Role
from ticketsApp.models.boxOffice import BoxOffice

admin.site.register(Role)
admin.site.register(User)
admin.site.register(BoxOffice)
admin.site.register(UserLoginActivity)
