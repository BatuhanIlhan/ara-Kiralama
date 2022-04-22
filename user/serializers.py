from datetime import datetime

from rest_framework.exceptions import ValidationError
from user.person_validation import is_valid_person
from rest_framework import serializers
from user.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['email']  # Doesn't raise error
        exclude = ["password"]

    # form validation beforehand

    def validate(self, data):
        if not is_valid_person(
                data["identity_number"],
                data["first_name"],
                data["last_name"],
                data["date_of_birth"].year):
            raise ValidationError(detail="Personal information is not matched with mernis")
        return data
