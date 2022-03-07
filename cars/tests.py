from http import HTTPStatus

import json
from django.http import HttpResponse
from django.test import TestCase
from model_bakery import baker
# Create your tests here.
from django.urls import reverse
from offices.models import Office
from cars.models import Car, CarModel, CarBrand


class CarRetrieveEndpointTests(TestCase):
    def setUp(self):
    #     self.office = Office.objects.create()
    #     self.carBrand = baker.make("cars.CarBrand")
    #     self.carModel = baker.make("cars.CarModel")
        self.car = baker.make("cars.Car")
        pass

    def test_retrieve_car_by_id_successfully(self):
        response = self.client.get(reverse("car:index") + f"{self.car.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"name": self.car.model.name, "brand": self.car.model.brand.name, "yil": self.car.model.year,
             "yakit tipi": self.car.fuel_type, "vites tipi": self.car.transmission_type,
             "koltuk sayisi": self.car.model.seat_count, "sinif": self.car.model.car_class}])

    def test_retrieve_car_that_does_not_exist(self):
        response = self.client.get(reverse("car:index") + "?id=-1")
        response_second = self.client.get(reverse("car:index") + "?id=5")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_second.status_code, 404)

    def test_delete_car_by_id(self):
        response = self.client.get(reverse("car:deleting"), data={"id": f"{self.car.id}"})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())
        self.assertEqual(response.json(), {"Car with id %s" % self.car.id: "Deleted"})

    def test_delete_car_that_does_not_exist(self):
        response = self.client.get(reverse("car:deleting") + "?id=-1")
        response_second = self.client.get(reverse("car:deleting") + "?id=10")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_second.status_code, 404)

    def test_create_car(self):
        body = {
            "transmission_type": "manuel",
            "fuel_type": "gasoline",
            "model": 1,
            "office": 1
        }
        encode_data = json.dumps(body).encode('utf-8')
        response = self.client.generic("GET", reverse("car:car_creating"), encode_data)
        self.assertEqual(response.json(), {"Car with id %s" % (self.car.id+1): "Created"})



