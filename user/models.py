import datetime

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


from cars.models import Car
# from reservation.models import Reservation


def phone_number_length_validator(value):
    if not value.isdigit():
        raise ValidationError(message="The phone number must consist of digits.")
    if len(value) != 10:
        raise ValidationError(message="The phone number must consist of exactly 10 digits.")
    return True


def date_of_birth_validator(value):
    if value > datetime.date.today():
        raise ValidationError(message="The date of birth cannot be in the future.")
    return True


def identity_number_length_validator(value):
    if not value.isdigit():
        raise ValidationError(message="The identity number must consist of digits.")
    if len(value) != 11:
        raise ValidationError(message="The identity number must consist of exactly 11 digits.")
    return True


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    identity_number = models.CharField(max_length=11,validators=[identity_number_length_validator])
    phone_number = models.CharField(max_length=10, validators=[phone_number_length_validator])
    date_of_birth = models.DateField(validators=[date_of_birth_validator])
    email_address = models.EmailField()
    password = models.CharField(max_length=50)

