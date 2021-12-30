from django.db import models

# Create your models here.

#class CarManager(models.Manager):
#    def create_car(self,markaa):
#        car = self.create(marka=markaa)
#        return car
class Car(models.Model):
    marka = models.CharField(max_length=50)
    modell = models.CharField(max_length=50)
    yil = models.IntegerField(default=2021)
    yakit_tipi = models.CharField(max_length=50)
    vites_tipi = models.CharField(max_length=50)
    koltuk_sayisi = models.IntegerField(default=5)
    sinif = models.CharField(max_length=50)
   # pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.marka + " " + self.modell
#    objects = CarManager()

