from django.urls import path
from . import views

app_name = "car"
urlpatterns = [
    path("<int:car_id>", views.retrieving_car_by_id , name="index"),
    path("", views.retrieving_cars , name="index"),
    # path("create/carmodel/", views.create_car_model, name="CarModel_creating"),
    # path("create/carbrand/", views.create_car_brand, name="CarBrand_creating"),
    # path("edit/", views.edit_car, name="car_editing"),
    # path("rand/<int:car_id>",views.randd,name="sdf")

]
