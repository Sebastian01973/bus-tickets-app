from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

from .user import User


class BoxOfficeManager(BaseUserManager):
    def create_box_office(self, username, password):
        """
        Creates and saves a BoxOffice with the given username and password.
        """
        if not username:
            raise ValueError("Username must be provided")
        box_office = self.model(username=username)
        box_office.set_password(password)
        box_office.save(using=self._db)
        return box_office

    def create_superbox_office(self, username, password):
        """
        Creates and saves a superofficebox with the given username and password.
        """
        box_office = self.create_box_office(username=username, password=password)
        box_office.is_admin = True
        box_office.save(using=self._db)
        return box_office


class BoxOffice(AbstractBaseUser, PermissionsMixin):
    """
        This model represents a Box Office in the company.
        with and id that automatically increments and foreingkey of User
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=256)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = BoxOfficeManager()
    USERNAME_FIELD = 'username'

