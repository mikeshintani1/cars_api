from operator import mod
from django.db import models

# Create your models here.
# max length is required for all CharField
# This is essentially the blue print for what fields will be input/displayed for cars
class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
# integer field does not require a limit
    year = models.IntegerField()
# max digits in decimal form will limit numbers for or after decimal!
    price = models.DecimalField(max_digits=8, decimal_places=2)