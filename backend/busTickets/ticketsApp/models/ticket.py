from django.db import models

from .client import Client
from .boxOffice import BoxOffice
from .vehicle import Vehicle
from .road import Road


class Ticket(models.Model):
    """
    This model represents a Ticket in the company.
    with and id that automatically increments and foreingkey of client, boxOffice, vehicle and road
    """
    id = models.BigAutoField(primary_key=True, unique=True, null=False)
    generate_date = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField(null=False)
    quantity = models.IntegerField(default=1, null=False)
    state = models.BooleanField(default=True, null=False)
    total_value = models.FloatField(null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    box_office = models.ForeignKey(BoxOffice, on_delete=models.CASCADE, null=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False)
    road = models.ForeignKey(Road, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.id

