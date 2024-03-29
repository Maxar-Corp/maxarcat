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

class Collection(object):
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
        'description': 'str',
        'id': 'str',
        'links': 'Links',
        'stac_version': 'str',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'links': 'links',
        'stac_version': 'stac_version',
        'title': 'title'
    }

    def __init__(self, description=None, id=None, links=None, stac_version=None, title=None):  # noqa: E501
        """Collection - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._id = None
        self._links = None
        self._stac_version = None
        self._title = None
        self.discriminator = None
        self.description = description
        self.id = id
        if links is not None:
            self.links = links
        self.stac_version = stac_version
        if title is not None:
            self.title = title

    @property
    def description(self):
        """Gets the description of this Collection.  # noqa: E501


        :return: The description of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Collection.


        :param description: The description of this Collection.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this Collection.  # noqa: E501


        :return: The id of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Collection.


        :param id: The id of this Collection.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def links(self):
        """Gets the links of this Collection.  # noqa: E501


        :return: The links of this Collection.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Collection.


        :param links: The links of this Collection.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def stac_version(self):
        """Gets the stac_version of this Collection.  # noqa: E501


        :return: The stac_version of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._stac_version

    @stac_version.setter
    def stac_version(self, stac_version):
        """Sets the stac_version of this Collection.


        :param stac_version: The stac_version of this Collection.  # noqa: E501
        :type: str
        """
        if stac_version is None:
            raise ValueError("Invalid value for `stac_version`, must not be `None`")  # noqa: E501

        self._stac_version = stac_version

    @property
    def title(self):
        """Gets the title of this Collection.  # noqa: E501


        :return: The title of this Collection.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Collection.


        :param title: The title of this Collection.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(Collection, dict):
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
        if not isinstance(other, Collection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
