# Create your views here.
from datetime import datetime
import json

from django import forms
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from reservation.models import Reservation
from user.models import User
from . import person_validation


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "name", "surname", "identity_number", "phone_number", "date_of_birth",
                  "email_address", "password"]


class UpdateForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    surname = forms.CharField(max_length=100, required=False)
    identity_number = forms.CharField(max_length=11, required=False)
    phone_number = forms.CharField(required=False)
    date_of_birth = forms.DateField(required=False)
    email_address = forms.EmailField(required=False)
    password = forms.CharField(max_length=50, required=False)

    def clean_date_of_birth(self):
        if self.cleaned_data["date_of_birth"] is None:
            self.cleaned_data.pop("date_of_birth")
        return self.cleaned_data


@csrf_exempt
def user_function_with_username(request, username):
    if request.method == "GET":
        return retrieve_user(request, username)

    elif request.method == "DELETE":
        return delete_user(request, username)

    elif request.method == "PUT":
        return update_user(request, username)
    else:
        return HttpResponse(status=400)


@csrf_exempt
def user_function(request):
    if request.method == "GET":
        return retrieve_all_user(request)
    elif request.method == "POST":
        return create_user(request)
    else:
        return HttpResponse(status=400)


def retrieve_user(request, username):
    user = get_object_or_404(User, username=username)
    rental_history = []
    for reservation in Reservation.objects.filter(user=user):
        rental_history.append(reservation.id)
    return JsonResponse(
        {"name": user.name, "surname": user.surname,
         "identity_number": user.identity_number, "rental history": rental_history})


def delete_user(request, username):
    user = get_object_or_404(User, username=username)
    user.delete()
    return JsonResponse({"User %s" % username: "Deleted"})


def retrieve_all_user(request):
    list_of_user = []
    for user in User.objects.all():
        list_of_user.append(user.username)
    return JsonResponse(list_of_user, safe=False)


def create_user(request):
    try:
        request_body = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(content=json.JSONDecodeError, status=400)
    form = UserForm(data=request_body)
    if not form.is_valid():
        return HttpResponse(content=dict(form.errors.items()), status=400)

    validate_person = person_validation.are_valid_person(
        request_body["identity_number"],
        request_body["name"],
        request_body["surname"],
        datetime.strptime(request_body["date_of_birth"], "%Y-%m-%d").year)
    if not validate_person:
        return HttpResponse(content="invalid person")
    new_user = form.save()
    return JsonResponse({f"new user {new_user.name}": "Created"})


@csrf_exempt
def login(request, username):
    if request.method == "POST":
        try:
            request_body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(content=json.JSONDecodeError, status=400)

        user = get_object_or_404(User, username=username)
        try:
            password = request_body["password"]
        except KeyError as error:
            return HttpResponse(content=error, status=400)

        if password != user.password:
            return HttpResponse(content="wrong password or username", status=400)
        return redirect(f"/user/{user.username}")


def update_user(request, username):
    try:
        request_body = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(content=json.JSONDecodeError, status=400)
    form = UpdateForm(request_body)
    if not form.is_valid():
        return HttpResponse(content=dict(form.errors.items()), status=400)
    User.objects.filter(username=username).update(**form.cleaned_data)
    return JsonResponse({"passs":    ""})

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
