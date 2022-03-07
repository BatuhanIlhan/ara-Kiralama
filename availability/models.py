from django.db import models
from cars.models import Car

# Create your models here.
from user.models import User


class Unavailability(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_datetime = models.DateField()
    end_datetime = models.DateField()
    user = models.ForeignKey(User, models.CASCADE, blank=True,null=True)
