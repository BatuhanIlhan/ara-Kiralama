import json
from django import forms
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cars.models import Car


# Create your views here.
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        # fields = ["transmission_type", "fuel_type", "model", "office"]
        fields = []


class CarUpdateForm(forms.Form):
    transmission_type = forms.CharField(max_length=50, required=False)
    fuel_type = forms.CharField(max_length=50, required=False)
    office = forms.IntegerField(required=False)
    model = forms.IntegerField(required=False)


@csrf_exempt
def car_functions_with_id(request, car_id):
    if request.method == "GET":
        if Car.objects.filter(id=car_id).exists():
            car = Car.objects.get(id=car_id)
            context = {"name": car.model.name, "brand": car.model.brand.name, "yil": car.model.year,
                       "yakit tipi": car.fuel_type, "vites tipi": car.transmission_type,
                       "koltuk sayisi": car.model.seat_count, "sinif": car.model.car_class}
            return JsonResponse(context)
        else:
            return HttpResponse(content="Car with id %s does not exist" % car_id, status=404)
    elif request.method == "DELETE":
        if Car.objects.filter(id=car_id).exists():
            car = Car.objects.get(id=car_id)
            car.delete()
            return JsonResponse({"Car with id %s" % car_id: "Deleted"})
        else:
            return HttpResponse(content="Car with id %s does not exist" % car_id, status=404)
    elif request.method == "POST":
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(content="JSONDecodeError", status=400)
        if not Car.objects.filter(id=car_id).exists():
            return HttpResponse(content="Car with id %s does not exist" % car_id, status=404)
        form = CarUpdateForm(request_body)
        if not form.is_valid():
            return HttpResponse(content=dict(form.errors.items()), status=400)
        n = {}
        for key, value in form.cleaned_data.items():
            if value:
                n[key] = value
        Car.objects.filter(id=car_id).update(**n)
        return JsonResponse({"Car with id %s" % car_id: "Edited"})


@csrf_exempt
def car_functions(request):
    if request.method == "GET":
        context = []
        for car in Car.objects.all():
            context.append({"name": car.model.name, "brand": car.model.brand.name, "yil": car.model.year,
                            "yakit tipi": car.fuel_type, "vites tipi": car.transmission_type,
                            "koltuk sayisi": car.model.seat_count, "sinif": car.model.car_class})
        return JsonResponse(context, safe=False)

    elif request.method == "POST":
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(content="JSONDecodeError", status=400)
        form = CarForm(data=request_body)
        if not form.is_valid():
            return HttpResponse(content=dict(form.errors.items()), status=400)
        new_car_model = form.save()
        return JsonResponse({"Car with id %s" % new_car_model.id: "Created"})

    # def index(request):
#     if request.GET.get("id"):
#         if Car.objects.filter(pk=request.GET.get("id")).exists():
#             cars_list = Car.objects.filter(pk=request.GET.get("id"))
#         else:
#             return HttpResponse(status=404)
#     else:
#         cars_list = Car.objects.all()
#     context = []
#     for car in cars_list:
#         context.append({"name": car.model.name, "brand": car.model.brand.name, "yil": car.model.year,
#                         "yakit tipi": car.fuel_type, "vites tipi": car.transmission_type,
#                         "koltuk sayisi": car.model.seat_count, "sinif": car.model.car_class})
#     return JsonResponse(context, safe=False)
#
#
# @csrf_exempt
# def delete_car(request):
#     if request.GET.get("id") is None:
#         return HttpResponse("missing id parameter", content_type='text/plain', status=400)
#
#     try:
#         car = Car.objects.get(id=request.GET.get("id"))
#         car.delete()
#         dic = {"Car with id %s" % request.GET.get("id"): "Deleted"}
#     except Car.DoesNotExist:
#         return HttpResponse(status=404)
#     return JsonResponse(dic, safe=False)
#
#
# class CarForm(forms.ModelForm):
#     class Meta:
#         model = Car
#         fields = ["transmission_type", "fuel_type", "model", "office"]
#
#
# @csrf_exempt
# def create_car(request):
#     try:
#         dic = json.loads(request.body)
#     except json.JSONDecodeError:
#         return HttpResponse(status=400)
#     form = CarForm(data=dic)
#     if not form.is_valid():
#         return HttpResponse(content=dict(form.errors.items()), status=400)
#     new_car = form.save()
#
#     return JsonResponse({"Car with id %s" % new_car.id: "Created"})
#
#
# class CarModelForm(forms.ModelForm):
#     class Meta:
#         model = CarModel
#         fields = ["name", "year", "seat_count", "car_class", "brand"]
#
#
# @csrf_exempt
# def create_car_model(request):
#     try:
#         dic = json.loads(request.body)
#     except json.JSONDecodeError:
#         return HttpResponse(status=400)
#     form = CarModelForm(data=dic)
#     if not form.is_valid():
#         return HttpResponse(content=dict(form.errors.items()), status=400)
#     new_car_model = form.save()
#     return JsonResponse({"Car Model with id %s" % new_car_model.id: "Created"}, safe=False)
#
#
# class CarBrandForm(forms.ModelForm):
#     class Meta:
#         model = CarBrand
#         fields = ["name"]
#
#
# @csrf_exempt
# def create_car_brand(request):
#     try:
#         dic = json.loads(request.body)
#     except json.JSONDecodeError:
#         return HttpResponse(status=400)
#     form = CarBrandForm(data=dic)
#     new_car_brand = form.save()
#     return JsonResponse({"Car Brand with id %s" % new_car_brand.id: "Created"}, safe=False)
#
#
# @csrf_exempt
# def edit_car(request):
#     dic = json.loads(request.body)
#     car = Car.objects.get(id=dic["id"])
#     if dic.get("transmission_type") is not None:
#         car.transmission_type = dic["transmission_type"]
#     if dic.get("fuel_type") is not None:
#         car.fuel_type = dic["fuel_type"]
#     if dic.get("model_id") is not None:
#         car.model_id = dic["model_id"]
#     if dic.get("office_id") is not None:
#         car.office_id = dic["office_id"]
#     car.save()
#     return JsonResponse({"Car with id %s" % car.id: "Edited"})
#
#
# def randd(request, car_id):
#     if request.method=="GET":
#         return JsonResponse({"car": car_id})
