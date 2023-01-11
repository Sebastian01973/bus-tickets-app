from django.db import models


class Payroll(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    date = models.DateField(null=False)
    discount = models.CharField(max_length=20, null=False)
    retention = models.FloatField(null=False)


    def __str__(self):
        return self.date
