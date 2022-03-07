from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from model_bakery import baker

from availability.models import Unavailability


class ReservationPostEndPointTests(TestCase):
    def setUp(self):
        self.office = baker.make("offices.Office")
        self.car = baker.make("cars.car")
        self.car.office_id = self.office.id
        self.car.save()
        pass

    def test_creation_of_unavailability(self):
        response = self.client.post(reverse("reservation:making_reservation"),
                                    data={"car": self.car.id, "start_datetime": "2022-12-1",
                                          "end_datetime": "2022-12-15",
                                          "officeId": self.office.id}, content_type="application/json")
        self.assertEqual(200, response.status_code)
        self.assertEqual({"reservationId": 1}, response.json())
