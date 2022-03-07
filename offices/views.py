import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from offices.models import Office


# Create your views here.

@csrf_exempt
def index(request):
    if request.method == "GET":
        return get_office(request)
    elif request.method == "POST":
        return create_or_edit_office(request)
    elif request.method == "DELETE":
        return delete_office(request)
    else:
        return HttpResponse(status=405)


def create_or_edit_office(request):
    try:
        dic = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(400)
    if dic.get("id") is not None:
        try:
            office = Office.objects.get(id=dic["id"])
            if dic.get("city") is not None:
                office.city = dic["city"]
            if dic.get("country") is not None:
                office.country = dic["country"]
            if dic.get("address") is not None:
                office.address = dic["address"]
                getattr(office,"address")
                setattr(office,"address",dic["address"])
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

    return JsonResponse(context, safe=False)


def get_office(request):
    if request.GET.get("id"):
        if Office.objects.filter(id=request.GET.get("id")).exists():
            office_list = Office.objects.filter(id=request.GET.get("id"))
            context = []
            for office in office_list:
                context.append({"ulke": office.country, "sehir": office.city, "adres": office.address})
            return JsonResponse(context, safe=False)
        else:
            return HttpResponse(status=404)


def delete_office(request):
    try:
        dic = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(status=400)

    try:
        office = Office.objects.get(id=dic["id"])
        office.delete()
        context = {"Office with id %s" % dic["id"]: "Deleted"}
        return JsonResponse(context, safe=False)
    except Office.DoesNotExist:
        return HttpResponse(status=404)
