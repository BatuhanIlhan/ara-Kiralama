from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from offices.models import Office


class OfficeSerializers(serializers.ModelSerializer):
    def validate(self, data):
        if data.get("phone_number") is not None and data["phone_number"][0] == '5':
            raise ValidationError(detail="phone number cannot starts with 5", code=1003)
        return data

    class Meta:
        model = Office
        fields = ["id", "country", "city", "address", "phone_number"]
