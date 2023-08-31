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
from maxarcat_client.api.maxar_extensionsubcatalog_api import MAXAREXTENSIONSUBCATALOGApi  # noqa: E501
from maxarcat_client.rest import ApiException


class TestMAXAREXTENSIONSUBCATALOGApi(unittest.TestCase):
    """MAXAREXTENSIONSUBCATALOGApi unit test stubs"""

    def setUp(self):
        self.api = MAXAREXTENSIONSUBCATALOGApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sub_catalog(self):
        """Test case for get_sub_catalog

        Get sub-catalog definition  # noqa: E501
        """
        pass

    def test_get_sub_catalog_collection(self):
        """Test case for get_sub_catalog_collection

        Get Collection in a Sub-Catalog  # noqa: E501
        """
        pass

    def test_get_sub_catalog_item(self):
        """Test case for get_sub_catalog_item

        Get Sub-Catalog STAC Item  # noqa: E501
        """
        pass

    def test_get_sub_catalog_search(self):
        """Test case for get_sub_catalog_search

        Search Sub-Catalog STAC items with filtering.  # noqa: E501
        """
        pass

    def test_list_sub_catalog_collection_items(self):
        """Test case for list_sub_catalog_collection_items

        List Items in a Sub-Catalog's collection  # noqa: E501
        """
        pass

    def test_list_sub_catalog_collections(self):
        """Test case for list_sub_catalog_collections

        List Sub-Catalog Collections  # noqa: E501
        """
        pass

    def test_list_sub_catalogs(self):
        """Test case for list_sub_catalogs

        List top level Maxar Sub-Catalogs  # noqa: E501
        """
        pass

    def test_post_sub_catalog_search(self):
        """Test case for post_sub_catalog_search

        Search Sub-Catalog STAC items with filtering.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
