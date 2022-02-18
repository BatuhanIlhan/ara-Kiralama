from django.urls import path
from . import views

urlpatterns = [
    path("mkmk", views.index, name="making_reservation")
]
