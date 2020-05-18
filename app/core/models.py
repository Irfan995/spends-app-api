from django.db import models
from django.conf import settings
# Create your models here.

class Spend(models.Model):
    """
    Spend object
    """
    item = models.CharField(max_length=255)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__():
        return self.item
