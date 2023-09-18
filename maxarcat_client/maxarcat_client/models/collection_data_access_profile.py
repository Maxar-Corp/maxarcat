# coding: utf-8

"""
    Maxar MGP Discovery API

    The Maxar MGP Discovery API implements a STAC-compliant service for searching the Maxar content catalog.  __The STAC specification is still under development.  When version 1.0 of the STAC specification is released the Discovery API will be updated to reflect any changes, some of which may not be backward compatible with this current version.__  For information on STAC see [stacspec.org](https://stacspec.org)   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CollectionDataAccessProfile(object):
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
        'policies': 'list[DataAccessPolicy]'
    }

    attribute_map = {
        'policies': 'policies'
    }

    def __init__(self, policies=None):  # noqa: E501
        """CollectionDataAccessProfile - a model defined in Swagger"""  # noqa: E501
        self._policies = None
        self.discriminator = None
        self.policies = policies

    @property
    def policies(self):
        """Gets the policies of this CollectionDataAccessProfile.  # noqa: E501


        :return: The policies of this CollectionDataAccessProfile.  # noqa: E501
        :rtype: list[DataAccessPolicy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this CollectionDataAccessProfile.


        :param policies: The policies of this CollectionDataAccessProfile.  # noqa: E501
        :type: list[DataAccessPolicy]
        """
        if policies is None:
            raise ValueError("Invalid value for `policies`, must not be `None`")  # noqa: E501

        self._policies = policies

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
        if issubclass(CollectionDataAccessProfile, dict):
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
        if not isinstance(other, CollectionDataAccessProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
