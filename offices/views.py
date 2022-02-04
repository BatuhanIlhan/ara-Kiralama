import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from offices.models import Office


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "GET":
        if request.GET.get("id"):
            office_list = Office.objects.filter(id=request.GET.get("id"))
        else:
            office_list = Office.objects.all()
        context = []
        for office in office_list:
            context.append({"ulke": office.country, "sehir": office.city, "adres": office.address})
    elif request.method == "POST":
        dic = json.loads(request.body)
        if dic.get("id") is not None:
            try:
                office = Office.objects.get(id=dic["id"])
                if dic.get("city") is not None:
                    office.city = dic["city"]
                if dic.get("country") is not None:
                    office.country = dic["country"]
                if dic.get("address") is not None:
                    office.address = dic["address"]
                office.save()
                context = {"Office with id %s" % office.id: "Edited"}
            except Office.DoesNotExist:
                context = {"Office with id %s" % dic["id"]: "Does Not Exist"}

        else:
            new_office = Office(country=dic["country"],
                                city=dic["city"],
                                address=dic["address"]
                                )
            new_office.save()
            context = {"Office with id %s" % new_office.id: "Created"}
    elif request.method == "DELETE":
        dic = json.loads(request.body)
        try:
            office = Office.objects.get(id=dic["id"])
            office.delete()
            context = {"Office with id %s" % dic["id"]: "Deleted"}
        except Office.DoesNotExist:
            context = {"Office with id %s" % dic["id"]: "Does Not Exist"}
    else:
        context = {}

    return JsonResponse(context, safe=False)
