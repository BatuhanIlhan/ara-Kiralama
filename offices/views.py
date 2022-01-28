from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from offices.models import Office


def index(request):
    if request.GET.get("id"):
        office_list =Office.objects.filter(id=request.GET.get("id"))
    else:
        office_list = Office.objects.all()
    context = []
    for office in office_list:
        context.append({"ulke": office.country,"sehir":office.city,"adres":office.address})

    return JsonResponse(context, safe=False)


