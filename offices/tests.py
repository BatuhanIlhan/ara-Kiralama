import json

from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
import random


# Create your tests here.
class OfficeRetrieveEndpointTests(TestCase):
    def setUp(self):
        self.offices = []
        for n in range(4):
            self.offices.append(baker.make("offices.Office"))

    def test_retrieve_office_by_id(self):
        n = random.randint(0, 3)
        response = self.client.get(reverse("office:index") + f"?id={self.offices[n].id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [{"ulke": self.offices[n].country, "sehir": self.offices[n].city,
                           "adres": self.offices[n].address}])

    def test_retrieve_office_that_does_not_exist(self):
        response = self.client.get(reverse("office:index") + f"?id={0}")
        self.assertEqual(response.status_code, 404)


class OfficeDeleteEndpointTests(TestCase):
    def setUp(self):
        self.offices = []
        for n in range(4):
            self.offices.append(baker.make("offices.Office"))


    def test_delete_office_by_id(self):
        n = random.randint(1, 4)
        response = self.client.delete(reverse("office:index"), data={"id": n}, content_type="application/json")
        self.assertEqual(200, response.status_code)
        self.assertEqual(404, self.client.get("office:index", {"id": n}).status_code)

    def test_delete_office_that_does_not_exist(self):
        response = self.client.delete(reverse("office:index"), data={"id": 0}, content_type="application/json")
        self.assertEqual(404, response.status_code)


class OfficePostEndpointTests(TestCase):
    def setUp(self):
        baker.make("offices.Office")


    def test_creating_car(self):
        response = self.client.post(reverse("office:index"), data={"country": "Turkey", "city": "Corum",
                                                                   "address": "assdıoajsda 8 88 dsa osd pasd"},
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Office with id 2": "Created"})


