from django.db import models

from ticketsApp.models import BoxOffice
from ticketsApp.models.vehicle import Vehicle


class Payroll(models.Model):
    """
    This model represents a Payroll in the company.
    with and id that automatically increments and foreingkey of boxOffice and vehicle
    """
    id = models.AutoField(primary_key=True, unique=True, null=False)
    date = models.DateField(null=False)
    retention = models.FloatField(null=False)
    date_start = models.TimeField(null=False)
    date_end = models.TimeField(null=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    boxOffice = models.ForeignKey(BoxOffice, on_delete=models.CASCADE)

    def __str__(self):
        return self.id, ' ', self.date, ' ', self.retention, ' ', self.date_start, ' ', self.date_end, ' ', self.vehicle
