from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from ticketsApp.models import User


class BoxOfficeManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        sudo = self.create_user(username, email, password=password)
        sudo.is_admin = True
        sudo.is_staff = True
        sudo.is_superuser = True
        sudo.save(using=self._db)
        return sudo


class BoxOffice(AbstractBaseUser, PermissionsMixin):
    """
        This model represents a Box Office in the company.
        with and id that automatically increments and foreingkey of User
    """
    id(models.AutoField(primary_key=True))
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    def save(self, **kwargs):
        """
        Hash the password before saving the BoxOffice model
        """
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = BoxOfficeManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
