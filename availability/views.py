from datetime import datetime

from django.http import JsonResponse
# Create your views here.
from availability.models import Unavailability
from cars.models import Car


# def index(request):
#     if request.GET.get("id"):
#         try:
#             car = Car.objects.get(id=request.GET.get("id"))
#             try:
#                 unavailability_list = Unavailability.objects.filter(car_id=car.id)
#                 dic = []
#                 for unavailability in unavailability_list:
#                     dic.append({"office": car.office_id, "start time": unavailability.start_datetime,
#                                 "end time": unavailability.end_datetime})
#             except Unavailability.DoesNotExist:
#                 dic = {"{}".format(car.id): "available"}
#         except Car.DoesNotExist:
#             dic = {"car with id %s" % request.GET.get("id"): "Does Not Exist"}
#
#     else:
#         if request.GET.get("date"):
#
#             date = request.GET.get("date")
#
#         else:
#             date = timezone.datetime.date(timezone.datetime.now())
#
#         dic = []
#         car_list = Car.objects.all()
#         unav = Unavailability.objects.all()
#         print(type(unav[0].end_datetime))
#
#         for car in car_list:
#             try:
#                 cur_car = Unavailability.objects.get(car_id=car)
#                 if cur_car.end_datetime < date:
#                     dic.append({"office": car.office.city, "name": car.model.name})
#             except Unavailability.DoesNotExist:
#                 dic.append({"office": car.office.city, "name": car.model.name})
#
#     return JsonResponse(dic, safe=False)

def index(request):
    officeId = request.GET.get("officeId")
    cars_of_the_office = Car.objects.filter(office_id=officeId)
    pickup_date = datetime.strptime(request.GET.get("pickupDate"), "%Y-%m-%d").date()
    dropoff_date = datetime.strptime(request.GET.get("dropoffDate"), "%Y-%m-%d").date()
    dic = []
    for car in cars_of_the_office:
        is_unavailable = Unavailability.objects.filter(
            car_id=car.id,
            end_datetime__lte=pickup_date,
            start_datetime__gte=pickup_date
        ).filter(
            end_datetime__lte=dropoff_date,
            start_datetime__gte=dropoff_date
        ).exists()

        if not is_unavailable:
            dic.append({
                "id": car.id,
                "transmission_type": car.transmission_type,
                "fuel_type": car.fuel_type,
                "model": car.model.name,
                "brand": car.model.brand.name
            })

    return JsonResponse(dic, safe=False)
