from django.db import models


class Business(models.Model):
    """
    This model represents a Business in the company. with and id that automatically increments
    """
    nit = models.CharField(primary_key=True, max_length=25, unique=True)
    name = models.CharField(max_length=50)
    withholding_tax = models.FloatField(max_length=10)
    business_code = models.CharField(max_length=10, unique=True, null=False)

    def __str__(self):
        return self.name, ' ', self.nit, ' ', self.withholding_tax, ' ', self.business_code
