import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cars.models import Car, CarModel, CarBrand


# Create your views here.


def index(request):
    if request.GET.get("id"):
        cars_list = Car.objects.filter(pk=request.GET.get("id"))
    else:
        cars_list = Car.objects.all()
    context = []
    for car in cars_list:
        context.append({"name": car.model_id.name, "brand": car.model_id.brand_id.name, "yil": car.model_id.yil,
                        "yakit tipi": car.fuel_type, "vites tipi": car.transmission_type,
                        "koltuk sayisi": car.model_id.seat_count, "sinif": car.model_id.car_class})

    return JsonResponse(context, safe=False)


@csrf_exempt
def delete_car(request):
    try:
        car = Car.objects.get(id=request.GET.get("id"))
        car.delete()
        dic = {"Car with id %s" % car.id: "Deleted"}
    except Car.DoesNotExist:
        dic = {"Car with id %s" % request.GET.get("id"): "Does not exist"}
    return JsonResponse(dic, safe=False)


@csrf_exempt
def create_car(request):
    dic = json.loads(request.body)
    new_car = Car(transmission_type=dic["transmission_type"],
                  fuel_type=dic["fuel_type"],
                  model_id=dic["model_id"],
                  office_id=dic["office_id"]
                  )
    new_car.save()
    return JsonResponse({"Car with id %s" % new_car.id: "Created"}, safe=False)


@csrf_exempt
def create_car_model(request):
    dic = json.loads(request.body)
    new_car_model = CarModel(year=dic["year"],
                             name=dic["name"],
                             seat_count=dic["seat_count"],
                             car_class=dic["car_class"],
                             brand_id=dic["brand_id"]
                             )
    new_car_model.save()
    return JsonResponse({"Car Model with id %s" % new_car_model.id: "Created"}, safe=False)


@csrf_exempt
def create_car_brand(request):
    dic = json.loads(request.body)
    new_car_brand = CarBrand(name=dic["name"])
    new_car_brand.save()
    return JsonResponse({"Car Brand with id %s" % new_car_brand.id: "Created"}, safe=False)


@csrf_exempt
def edit_car(request):
    dic = json.loads(request.body)
    car = Car.objects.get(id=dic["id"])
    if dic.get("transmission_type") is not None:
        car.transmission_type = dic["transmission_type"]
    if dic.get("fuel_type") is not None:
        car.fuel_type = dic["fuel_type"]
    if dic.get("model_id") is not None:
        car.model_id = dic["model_id"]
    if dic.get("office_id") is not None:
        car.office_id = dic["office_id"]
    car.save()
    return JsonResponse({"Car with id %s" % car.id: "Edited"}, safe=False)
