from django.db import models


class Road(models.Model):
    """
    This model represents a Road in the company. with and id that automatically increments
    """
    id = models.AutoField(primary_key=True, unique=True, null=False)
    destiny = models.CharField(max_length=25)
    ticket_value = models.FloatField(null=False, default=0)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.id, ' ', self.destiny, ' ', self.ticket_value, ' ', self.code
