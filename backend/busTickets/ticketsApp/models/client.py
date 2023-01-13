from django.db import models

from .user import User


class Client(models.Model):
    """
        This model represents a Client of the company.
        with and id that automatically increments and foreingkey of User
    """
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)