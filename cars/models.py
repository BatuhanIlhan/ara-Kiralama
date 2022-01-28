from django.db import models

from offices.models import Office


# Create your models here.









#    objects = CarManager()
class CarBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)



class CarModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    yil = models.IntegerField(default=2021)

    seat_count = models.IntegerField(default=5)
    car_class = models.CharField(max_length=50)
    brand_id = models.ForeignKey(CarBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    transmission_type = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    model_id= models.ForeignKey(CarModel, on_delete=models.CASCADE)
    office_id= models.ForeignKey(Office,on_delete=models.CASCADE)
