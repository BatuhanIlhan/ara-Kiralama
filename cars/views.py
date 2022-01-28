from django.http import JsonResponse, HttpResponse, Http404

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from cars.models import Car


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


def delete_car(request):
    try:
        car = Car.objects.get(id=request.GET.get("id"))
        car.delete()
    except:
        raise Http404("Car does not exist")
    return HttpResponse(car)

@csrf_exempt
def create_car(request):
    car = Car(marka="Toyota", modell="Corolla")
    car.save()
    return HttpResponse(car)
