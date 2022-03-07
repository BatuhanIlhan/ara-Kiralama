from . import views
from django.urls import path
app_name = "office"
urlpatterns = [
    path("", views.index, name="index"),
]
