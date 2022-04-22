# coding: utf-8

"""
    Car Rental Api

    Rest api for car rental  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: mabtuhanilhan@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Car(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'transmission_type': 'str',
        'fuel_type': 'str',
        'model': 'CarModel'
    }

    attribute_map = {
        'id': 'id',
        'transmission_type': 'transmission_type',
        'fuel_type': 'fuel type',
        'model': 'model'
    }

    def __init__(self, id=None, transmission_type=None, fuel_type=None, model=None, _configuration=None):  # noqa: E501
        """Car - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._transmission_type = None
        self._fuel_type = None
        self._model = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if transmission_type is not None:
            self.transmission_type = transmission_type
        if fuel_type is not None:
            self.fuel_type = fuel_type
        if model is not None:
            self.model = model

    @property
    def id(self):
        """Gets the id of this Car.  # noqa: E501

        uniq identifier  # noqa: E501

        :return: The id of this Car.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Car.

        uniq identifier  # noqa: E501

        :param id: The id of this Car.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def transmission_type(self):
        """Gets the transmission_type of this Car.  # noqa: E501


        :return: The transmission_type of this Car.  # noqa: E501
        :rtype: str
        """
        return self._transmission_type

    @transmission_type.setter
    def transmission_type(self, transmission_type):
        """Sets the transmission_type of this Car.


        :param transmission_type: The transmission_type of this Car.  # noqa: E501
        :type: str
        """

        self._transmission_type = transmission_type

    @property
    def fuel_type(self):
        """Gets the fuel_type of this Car.  # noqa: E501


        :return: The fuel_type of this Car.  # noqa: E501
        :rtype: str
        """
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, fuel_type):
        """Sets the fuel_type of this Car.


        :param fuel_type: The fuel_type of this Car.  # noqa: E501
        :type: str
        """

        self._fuel_type = fuel_type

    @property
    def model(self):
        """Gets the model of this Car.  # noqa: E501


        :return: The model of this Car.  # noqa: E501
        :rtype: CarModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Car.


        :param model: The model of this Car.  # noqa: E501
        :type: CarModel
        """

        self._model = model

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Car, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Car):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Car):
            return True

        return self.to_dict() != other.to_dict()
