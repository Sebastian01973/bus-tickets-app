from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(models.Model):
    pass
    # def create_user(self, username, password=None):
    #     if not username:
    #         raise ValueError('Users must have an email address')
    #     user = self.model(username=username)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_superuser(self, username, password):
    #     sudo = self.create_user(username, password=password)
    #     sudo.is_admin = True
    #     sudo.save(using=self._db)
    #     return sudo


# Define the class News.
# This class is used to create the table News in the database.
class MyUser(models.Model):
    pass
    # id(models.AutoField(primary_key=True))
    # name = models.CharField(max_length=50)
    # username = models.CharField(max_length=50, unique=True)
    # # email = models.EmailField()
    # password = models.CharField('Password', max_length=256)
    #
    # is_staff = models.BooleanField(default=True)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=True)
    #
    #
    # def __str__(self):
    #     return self.name
    #
    # def save(self, **kwargs):
    #     some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
    #     self.password = make_password(self.password, some_salt)
    #     super().save(**kwargs)
    #
    # objects = UserManager()
    # USERNAME_FIELD = 'username'
