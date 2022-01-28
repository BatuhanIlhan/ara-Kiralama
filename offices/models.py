from django.db import models


# Create your models here.
class Office(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=400)

    def __str__(self):
        return str(self.id)
