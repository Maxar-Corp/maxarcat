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

class ItemCollectionPost(object):
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
        'features': 'list[Item]',
        'links': 'ItemCollectionPostLinks',
        'type': 'str'
    }

    attribute_map = {
        'features': 'features',
        'links': 'links',
        'type': 'type'
    }

    def __init__(self, features=None, links=None, type=None):  # noqa: E501
        """ItemCollectionPost - a model defined in Swagger"""  # noqa: E501
        self._features = None
        self._links = None
        self._type = None
        self.discriminator = None
        self.features = features
        if links is not None:
            self.links = links
        self.type = type

    @property
    def features(self):
        """Gets the features of this ItemCollectionPost.  # noqa: E501


        :return: The features of this ItemCollectionPost.  # noqa: E501
        :rtype: list[Item]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this ItemCollectionPost.


        :param features: The features of this ItemCollectionPost.  # noqa: E501
        :type: list[Item]
        """
        if features is None:
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def links(self):
        """Gets the links of this ItemCollectionPost.  # noqa: E501


        :return: The links of this ItemCollectionPost.  # noqa: E501
        :rtype: ItemCollectionPostLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ItemCollectionPost.


        :param links: The links of this ItemCollectionPost.  # noqa: E501
        :type: ItemCollectionPostLinks
        """

        self._links = links

    @property
    def type(self):
        """Gets the type of this ItemCollectionPost.  # noqa: E501


        :return: The type of this ItemCollectionPost.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ItemCollectionPost.


        :param type: The type of this ItemCollectionPost.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["FeatureCollection"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(ItemCollectionPost, dict):
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
        if not isinstance(other, ItemCollectionPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
