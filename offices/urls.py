from . import views
from django.urls import path
app_name = "office"
urlpatterns = [
    path("<int:office_id>", views.OfficeViewWithId.as_view(), name="index"),
    path("", views.OfficeView.as_view(), name="index"),
]
