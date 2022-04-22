from django.db import models
from datetime import date
from offices.models import Office
from django.core.validators import MaxValueValidator


# Create your models here.


#    objects = CarManager()
class CarBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)


def max_year_validator(value):
    current_year = date.today().year
    return current_year >= value


class CarModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    year = models.IntegerField(validators=[max_year_validator], default=2021)
    seat_count = models.IntegerField(default=5)
    car_class = models.CharField(max_length=50)
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    transmission_type = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

