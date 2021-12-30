from django.http import JsonResponse, HttpResponse, Http404

# Create your views here.
from cars.models import Car


def index(request):
    if request.GET.get("id"):
        cars_list = Car.objects.filter(id=request.GET.get("id"))
    else:
        cars_list = Car.objects.all()
    context = []
    for car in cars_list:
        context.append({"name": car.marka, "brand": car.modell, "yil": car.yil,
                        "yakit tipi": car.yakit_tipi, "vites tipi": car.vites_tipi,
                        "koltuk sayisi": car.koltuk_sayisi, "sinif": car.sinif})

    return JsonResponse(context, safe=False)


def delete_car(request):
    try:
        car = Car.objects.get(id=request.GET.get("id"))
        car.delete()
    except:
        raise Http404("Question does not exist")
    return HttpResponse(car)


def create_car(request):
    car = Car(marka="Toyota", modell="Corolla")
    car.save()
    return HttpResponse(car)
