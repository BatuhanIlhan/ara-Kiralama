# Create your views here.
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from reservation.models import Reservation
from user.models import User
from user.serializers import UserSerializers

"""class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["identity_number", "phone_number", "date_of_birth"]
        not_editable = ["name", "surname", "identity_number", "date_of_birth"]"""

"""class UpdateForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    surname = forms.CharField(max_length=100, required=False)
    identity_number = forms.CharField(max_length=11, required=False)
    phone_number = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=False)
    email_address = forms.EmailField(required=False)
    password = forms.CharField(max_length=50, required=False)"""


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(content=json.JSONDecodeError, status=400)

        user = get_object_or_404(User, username=request_body.get("username"))
        print(request.session.values())
        login(request, user)
        print(request.session.values())
        try:
            password = request_body["password"]
        except KeyError as error:
            return HttpResponse(content=error, status=400)
        if not user.check_password(password):
            print(password)
            print(user.password)
            return HttpResponse(content="wrong password or username", status=400)

        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)


class UserMixin:
    @staticmethod
    def create_user(request):
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(content=json.JSONDecodeError, status=400)
        serializer = UserSerializers(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    @staticmethod
    def retrieve_user(request, username):
        user = get_object_or_404(User, username=username)
        rental_history = []
        for reservation in Reservation.objects.filter(user=user):
            rental_history.append(reservation.id)
        return JsonResponse(
            {"name": user.first_name, "surname": user.last_name,
             "identity_number": user.identity_number, "rental history": rental_history})

    @staticmethod
    def retrieve_all_user(request):
        users = User.objects.all()
        serializer = User(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    @staticmethod
    def update_user(request, username):
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(content=json.JSONDecodeError, status=400)
        user = get_object_or_404(User, username=username)
        serializer = UserSerializers(user, data=request_body, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    @staticmethod
    def delete_user(request, username):
        user = get_object_or_404(User, username=username)
        user.delete()
        return HttpResponse(status=204)


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View, UserMixin):
    def get(self, request):
        return self.retrieve_all_user(request)

    def post(self, request):
        return self.create_user(request)

    def put(self, request):
        request_body = json.loads(request.body)
        user = User.objects.get(username=request_body.get("username"))
        user.set_password(request_body.get("password"))
        user.save()
        return HttpResponse(status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserViewWithId(View, UserMixin):
    def get(self, request, username):
        return self.retrieve_user(request, username)

    def put(self, request, username):
        return self.update_user(request, username)

    def delete(self, request, username):
        return self.delete_user(request, username)


# {
#     "identity_number": "68674029192",
#     "name": "Muhammet Batuhan",
#     "surname": "ilhan",
#     "date_of_birth": "2001-09-11",
#     "username": "batuhanil4dhannn",
#     "phone_number": "5061041858",
#     "email_address": "mbatuhanilhan@gmail.com",
#     "password": "zxddsfadsf6."
# }

"""def update_user(request, username):
    try:
        request_body = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(content=json.JSONDecodeError, status=400)
    changed_fields = []
    for key in request_body:
        changed_fields.append(key)
        if key not in UserForm.Meta.fields:
            return HttpResponse(content=f"{key} is not a field of user", status=400)
        elif key in UserForm.Meta.not_editable:
            return HttpResponse(content=f"{key} is not editable field of user", status=400)

    User.objects.filter(username=username).update(**request_body)
    return JsonResponse({"These fields are updated": changed_fields})"""
