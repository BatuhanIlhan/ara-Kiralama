
from django.http import JsonResponse
# Create your views here.
from availability.models import Unavailability
from cars.models import Car
from django.utils import timezone



def index(request):
    if(request.GET.get("id")):
        try:
            car=Car.objects.get(id=request.GET.get("id"))
            try:
                unav = Unavailability.objects.get(car_id =car)
                dicc = {"office": car.office_id.id, "start time": unav.start_datetime,
                        "end time": unav.end_datetime}
            except:
                dicc = {"{}".format(car.id): "available"}
        except:
            dicc={}

    else:
        if request.GET.get("date"):

            date=request.GET.get("date")
            print(type(date))
        else :
            date= timezone.datetime.date(timezone.datetime.now())
            print(type(date))
        dicc=[]
        car_list= Car.objects.all()
        unav=Unavailability.objects.all()
        print(type(unav[0].end_datetime))

        for car in car_list:
            try:
                cur_car=Unavailability.objects.get(car_id=car)
                if cur_car.end_datetime < date:
                    dicc.append({"office": car.office_id.city, "name": car.model_id.name})
            except:
                dicc.append({"office" : car.office_id.city,"name": car.model_id.name})

    return JsonResponse(dicc,safe=False)