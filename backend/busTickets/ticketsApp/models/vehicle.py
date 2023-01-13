from django.db import models

from ticketsApp.models import Business, User


class Vehicle(models.Model):
    plate = models.CharField(primary_key=True, max_length=6, unique=True)
    internal_number = models.CharField(max_length=6, )
    capacity = models.IntegerField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.plate
