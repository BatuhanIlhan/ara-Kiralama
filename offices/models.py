from django.db import models


# Create your models here.
class Office(models.Model):
    ulke = models.CharField(max_length=50)
    sehir = models.CharField(max_length=50)
    adres = models.CharField(max_length=400)

    def __str__(self):
        return self.sehir + "/" + self.ulke
