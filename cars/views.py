import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cars.models import Car, CarModel, CarBrand


# Create your views here.


def index(request):
    if request.GET.get("id"):
        if Car.objects.filter(pk=request.GET.get("id")).exists():
            cars_list = Car.objects.filter(pk=request.GET.get("id"))
        else:
            return HttpResponse(status=404)
    else:
        cars_list = Car.objects.all()
    context = []
    for car in cars_list:
        context.append({"name": car.model.name, "brand": car.model.brand.name, "yil": car.model.year,
                        "yakit tipi": car.fuel_type, "vites tipi": car.transmission_type,
                        "koltuk sayisi": car.model.seat_count, "sinif": car.model.car_class})
    return JsonResponse(context, safe=False)


@csrf_exempt
def delete_car(request):
    try:
        car = Car.objects.get(id=request.GET.get("id"))
        car.delete()
        dic = {"Car with id %s" % request.GET.get("id"): "Deleted"}
    except Car.DoesNotExist:
        return HttpResponse(status=404)
    return JsonResponse(dic, safe=False)


@csrf_exempt
def create_car(request):
    try:
        dic = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(status=400)
    try:
        new_car = Car(transmission_type=dic["transmission_type"],
                      fuel_type=dic["fuel_type"],
                      model_id=dic["model_id"],
                      office_id=dic["office_id"]
                      )
    except :
        return HttpResponse(status=400)

    new_car.save()
    return JsonResponse({"Car with id %s" % new_car.id: "Created"})


@csrf_exempt
def create_car_model(request):
    try:
        dic = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(status=400)

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
