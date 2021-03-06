# coding: utf-8

"""
    Maxar Content API - Catalog

    The Maxar Content Catalog API implements a STAC-compliant service for searching the Maxar content catalog.  __The STAC specification is still under development.  When version 1.0 of the STAC specification is released the Content Catalog API will be updated to reflect any changes, some of which will not be backward compatible with this current version.__  For information on STAC see [stacspec.org](https://stacspec.org)   # noqa: E501

    OpenAPI spec version: 0.9
    Contact: DL-Content-Catalog@maxar.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import maxarcat_client
from maxarcat_client.api.stac_api import STACApi  # noqa: E501
from maxarcat_client.rest import ApiException


class TestSTACApi(unittest.TestCase):
    """STACApi unit test stubs"""

    def setUp(self):
        self.api = STACApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_healthcheck(self):
        """Test case for get_healthcheck

        Service healthcheck  # noqa: E501
        """
        pass

    def test_get_root(self):
        """Test case for get_root

        Return the root catalog or collection.  # noqa: E501
        """
        pass

    def test_get_search_stac(self):
        """Test case for get_search_stac

        Search STAC items with filtering.  # noqa: E501
        """
        pass

    def test_post_search_stac(self):
        """Test case for post_search_stac

        Search STAC items with full-featured filtering.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
