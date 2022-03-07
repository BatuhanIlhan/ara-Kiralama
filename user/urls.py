from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("<str:username>/login", views.login, name="login"),
    path("<str:username>", views.user_function_with_username, name="user_function_with_username"),
    path("", views.user_function, name="user_function"),
]
