# coding: utf-8

"""
    Car Rental Api

    Rest api for car rental  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mabtuhanilhan@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.car_api import CarApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCarApi(unittest.TestCase):
    """CarApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.car_api.CarApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cars_car_id_delete(self):
        """Test case for cars_car_id_delete

        Delete the car with the specified id  # noqa: E501
        """
        pass

    def test_cars_car_id_get(self):
        """Test case for cars_car_id_get

        Get the car with the specified id  # noqa: E501
        """
        pass

    def test_cars_car_id_post(self):
        """Test case for cars_car_id_post

        Update the car with the specified id  # noqa: E501
        """
        pass

    def test_cars_get(self):
        """Test case for cars_get

        Get list of all cars  # noqa: E501
        """
        pass

    def test_cars_post(self):
        """Test case for cars_post

        Create a new car  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()