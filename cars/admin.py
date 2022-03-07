from django.contrib import admin

# Register your models here.
from cars.models import Car, CarBrand, CarModel

admin.site.register(Car)
admin.site.register(CarBrand)
admin.site.register(CarModel)
