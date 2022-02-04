from django.contrib import admin

# Register your models here.
from reservation.models import Reservation

admin.site.register(Reservation)