from django.urls import path
from . import views
urlpatterns= [
    path("",views.index,name="index"),
    path("delete/", views.delete_car, name="deleting"),
    path("create/", views.create_car, name="creating"),


]