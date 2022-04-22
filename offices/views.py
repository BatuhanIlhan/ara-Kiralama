import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from offices.serializers import OfficeSerializers
from offices.models import Office
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.
class OfficeMixin(object):
    def log(self, request):
        print(f"request path: {request.path}")

    @staticmethod
    def get_list_office(request):
        offices = Office.objects.all()
        serializer = OfficeSerializers(offices, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def get_office_with_id(request, office_id):
        office = Office.objects.filter(id=office_id).first()
        if office:
            serializer = OfficeSerializers(office)
            return JsonResponse(serializer.data)
        else:
            return HttpResponse(status=404)

    @staticmethod
    def update_office(request, office_id):
        if Office.objects.filter(id=office_id).exists():
            try:
                dic = json.loads(request.body)
            except json.JSONDecodeError:
                return HttpResponse(400)
            office = Office.objects.get(id=office_id)
            serializer = OfficeSerializers(office, data=dic, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return HttpResponse(status=404)

    @staticmethod
    def create_office(request):
        try:
            dic = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(400)
        serializer = OfficeSerializers(data=dic)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    @staticmethod
    def delete_office(request, office_id):
        if Office.objects.filter(id=office_id).exists():
            office = Office.objects.get(id=office_id)
            office.delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=404)


@method_decorator(csrf_exempt, name='dispatch')
class OfficeView(View, OfficeMixin):
    def get(self, request):
        return self.get_list_office(request)

    def post(self, request):
        return self.create_office(request)


@method_decorator(csrf_exempt, name='dispatch')
class OfficeViewWithId(View, OfficeMixin):
    def get(self, request, office_id):
        return self.get_office_with_id(request, office_id)

    def put(self, request, office_id):
        return self.update_office(request, office_id)

    def delete(self, request, office_id):
        return self.delete_office(request, office_id)
