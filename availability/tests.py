from django.urls import reverse
from model_bakery import baker
from django.test import TestCase
from cars.views import edit_car
from cars.models import Car
from .models import Unavailability
from reservation.models import Reservation
from datetime import date


# Create your tests here.

class AvailabilityGetEndpointTests(TestCase):
    def setUp(self):
        self.office = baker.make("offices.Office")
        self.car = baker.make("cars.car")
        self.car.office_id = self.office.id
        self.car.save()
        self.unavailability_list = []
        unavailability_one = Unavailability(
            car_id=self.car.id,
            start_datetime=date(2022, 3, 15),
            end_datetime=date(2022, 3, 19)
        )
        unavailability_one.save()
        unavailability_two = Unavailability(
            car_id=self.car.id,
            start_datetime=date(2022, 3, 9),
            end_datetime=date(2022, 3, 11)
        )
        unavailability_two.save()

        pass

    def test_retrieve_an_available_car(self):
        response = self.client.get(reverse("availability:index"), {"officeId": self.office.id,
                                                                   "pickupDate": "2022-3-12",
                                                                   "dropoffDate": "2022-3-14"})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json()))
        self.assertEqual(response.json(), [{
            "id": self.car.id,
            "transmission_type": self.car.transmission_type,
            "fuel_type": self.car.fuel_type,
            "model": self.car.model.name,
            "brand": self.car.model.brand.name
        }])

    def test_retrieve_if_there_is_no_available_car(self):
        response = self.client.get(reverse("availability:index"), {"officeId": self.office.id,
                                                                   "pickupDate": "2022-3-11",
                                                                   "dropoffDate": "2022-3-14"})
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(response.json()))
        self.assertEqual(response.json(), [])
