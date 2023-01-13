from django.db import models


class Road(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    destiny = models.CharField(max_length=25)
    ticket_value = models.FloatField(null=False, default=0)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.destiny
