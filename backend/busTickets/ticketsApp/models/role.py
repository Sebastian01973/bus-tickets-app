from django.db import models


class Role(models.Model):
    """
        This model represents a Role in the company. with and id that automatically increments
    """
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name, ' - ', self.id_role
