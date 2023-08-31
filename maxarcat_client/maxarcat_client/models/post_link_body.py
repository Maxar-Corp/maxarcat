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

class PostLinkBody(object):
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
        'limit': 'float',
        'page': 'float'
    }

    attribute_map = {
        'limit': 'limit',
        'page': 'page'
    }

    def __init__(self, limit=None, page=None):  # noqa: E501
        """PostLinkBody - a model defined in Swagger"""  # noqa: E501
        self._limit = None
        self._page = None
        self.discriminator = None
        if limit is not None:
            self.limit = limit
        if page is not None:
            self.page = page

    @property
    def limit(self):
        """Gets the limit of this PostLinkBody.  # noqa: E501


        :return: The limit of this PostLinkBody.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PostLinkBody.


        :param limit: The limit of this PostLinkBody.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def page(self):
        """Gets the page of this PostLinkBody.  # noqa: E501


        :return: The page of this PostLinkBody.  # noqa: E501
        :rtype: float
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PostLinkBody.


        :param page: The page of this PostLinkBody.  # noqa: E501
        :type: float
        """

        self._page = page

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
        if issubclass(PostLinkBody, dict):
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
        if not isinstance(other, PostLinkBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other