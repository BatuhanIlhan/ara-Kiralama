import datetime

from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


from cars.models import Car


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


class User(AbstractUser):
    identity_number = models.CharField(max_length=11, validators=[identity_number_length_validator])
    phone_number = models.CharField(max_length=10, validators=[phone_number_length_validator])
    date_of_birth = models.DateField(validators=[date_of_birth_validator])
    REQUIRED_FIELDS = [identity_number, phone_number, date_of_birth]

