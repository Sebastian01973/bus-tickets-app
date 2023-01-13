from django.db import models

from ticketsApp.models import BoxOffice
from ticketsApp.models.vehicle import Vehicle


class Payroll(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    discount = models.CharField(max_length=20)
    retention = models.FloatField()
    date_start = models.DateField(auto_now=True)
    date_end = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    boxOffice = models.ForeignKey(BoxOffice, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
