import json

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from availability.models import Unavailability
from cars.models import Car
from reservation.models import Reservation


@csrf_exempt
def index(request):
    dic = json.loads(request.body)
    new_unavailability = Unavailability.objects.create(
        car_id=dic["carId"],
        start_datetime=dic["pickupDate"],
        end_datetime=dic["dropoffDate"]
    )

    car = Car.objects.get(id=dic["carId"])
    car.office_id = dic["officeId"]
    car.save()
    new_reservation = Reservation(
        office_id=dic["officeId"],
        car_id=dic["carId"],
        pick_up_date=dic["pickupDate"],
        drop_off_date=dic["dropoffDate"],
        unavailability=new_unavailability)
    new_reservation.save()

    return JsonResponse({"reservationId": new_reservation.id}, safe=False)
