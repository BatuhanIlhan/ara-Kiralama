import json

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from availability.models import Unavailability
from cars.models import Car
from reservation.models import Reservation
import datetime


class UnavailabilityForm(forms.ModelForm):
    class Meta:
        model = Unavailability
        fields = ["car", "start_datetime", "end_datetime", "user"]

    def clean_end_datetime(self):
        value = self.cleaned_data["end_datetime"]
        if datetime.date.today() > value:
            raise forms.ValidationError(message="end_time must be greater")
        return value

    def clean(self):
        value_start = self.cleaned_data["start_datetime"]
        value_end = self.cleaned_data["end_datetime"]
        if value_end < value_start:
            raise forms.ValidationError(message="end_time must be greater")
        return self.cleaned_data


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["office", "car", "pick_up_date", "drop_off_date", "unavailability", "user"]


@csrf_exempt
def index(request):
    try:
        dic = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(400)
    form = UnavailabilityForm(data=dic)
    if not form.is_valid():
        return HttpResponse(content=dict(form.errors.items()), status=400)

    new_unavailability = form.save()

    dic["unavailability"] = new_unavailability.id
    dic["pick_up_date"] = dic["start_datetime"]
    dic["drop_off_date"] = dic["end_datetime"]
    car = Car.objects.get(id=dic["car"])
    car.office_id = dic["office"]
    car.save()
    reservation_form = ReservationForm(data=dic)
    if not reservation_form.is_valid():
        return HttpResponse(content=dict(reservation_form.errors.items()), status=400)
    new_reservation = reservation_form.save()
    return JsonResponse({"reservationId": new_reservation.id})
