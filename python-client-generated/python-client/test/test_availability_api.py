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
from swagger_client.api.availability_api import AvailabilityApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAvailabilityApi(unittest.TestCase):
    """AvailabilityApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.availability_api.AvailabilityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_availability_get(self):
        """Test case for availability_get

        Cars available according to the given pick up and drop off date  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()