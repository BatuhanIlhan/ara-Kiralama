from django.test import TestCase

from cars.models import Car
from .models import Unavailability
from reservation.models import Reservation
from datetime import datetime


# Create your tests here.

class QuestionModelTests(TestCase):
    def test_unavailability_is_valid(self):
        unavailability = Unavailability(car_id=1, start_datetime=datetime.today().date(), end_datetime=datetime.today().date())
        self.assertIs(unavailability.end_datetime > unavailability.start_datetime, True)
