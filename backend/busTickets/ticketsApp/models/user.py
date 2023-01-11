from django.db import models
from .role import Role


class User(models.Model):
    """
        This model represents a User in the company.
        with and id that automatically increments and foreingkey of Role
    """
    id = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.id, ' ', self.identification, ' ', self.name, ' ', self.last_name, ' ', self.id_role

