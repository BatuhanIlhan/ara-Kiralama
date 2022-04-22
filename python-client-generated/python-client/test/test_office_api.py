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
from swagger_client.api.office_api import OfficeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOfficeApi(unittest.TestCase):
    """OfficeApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.office_api.OfficeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_offices_delete(self):
        """Test case for offices_delete

        Delete office with specsified id  # noqa: E501
        """
        pass

    def test_offices_get(self):
        """Test case for offices_get

        Get the office with specified id  # noqa: E501
        """
        pass

    def test_offices_post(self):
        """Test case for offices_post

        create or edit office  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
