from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path("login", views.login_user, name="login"),
    path("<str:username>", views.UserViewWithId.as_view(), name="user_function_with_username"),
    path("", views.UserView.as_view(), name="user_function"),
]
