from django.db import models

# Create your models here.
from availability.models import Unavailability
from cars.models import Car
from offices.models import Office


class Reservation(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    pick_up_date = models.DateField()
    drop_off_date = models.DateField()
    unavailability = models.OneToOneField(Unavailability, on_delete=models.CASCADE)

