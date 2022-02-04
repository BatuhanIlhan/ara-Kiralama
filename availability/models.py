from django.db import models
from cars.models import Car


# Create your models here.

class Unavailability(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_datetime = models.DateField()
    end_datetime = models.DateField()
