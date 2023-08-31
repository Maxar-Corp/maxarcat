# coding: utf-8

"""
    Maxar MGP Discovery API

    The Maxar MGP Discovery API implements a STAC-compliant service for searching the Maxar content catalog.  __The STAC specification is still under development.  When version 1.0 of the STAC specification is released the Discovery API will be updated to reflect any changes, some of which may not be backward compatible with this current version.__  For information on STAC see [stacspec.org](https://stacspec.org)   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import maxarcat_client
from maxarcat_client.models.server_conformance import ServerConformance  # noqa: E501
from maxarcat_client.rest import ApiException


class TestServerConformance(unittest.TestCase):
    """ServerConformance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServerConformance(self):
        """Test ServerConformance"""
        # FIXME: construct object with mandatory attributes with example values
        # model = maxarcat_client.models.server_conformance.ServerConformance()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
