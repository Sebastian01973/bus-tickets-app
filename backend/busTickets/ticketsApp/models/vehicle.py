from django.db import models

from ticketsApp.models import Business


class Vehicle(models.Model):
    plate = models.CharField(primary_key=True, max_length=6, null=False, unique=True)
    internal_number = models.CharField(max_length=6, null=False)
    capacity = models.IntegerField(null=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.plate
