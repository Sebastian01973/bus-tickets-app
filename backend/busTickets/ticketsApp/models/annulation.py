from django.db import models

from ticketsApp.models import Ticket


class Annulation(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, null=False)
    date_annulation = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=1000, null=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=False)
