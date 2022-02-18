from django.urls import path
from . import views

app_name = "car"
urlpatterns = [
    path("", views.index, name="index"),
    path("delete/", views.delete_car, name="deleting"),
    path("create/car/", views.create_car, name="car_creating"),
    path("create/carmodel/", views.create_car_model, name="CarModel_creating"),
    path("create/carbrand/", views.create_car_brand, name="CarBrand_creating"),
    path("edit/", views.edit_car, name="car_editing")

]
