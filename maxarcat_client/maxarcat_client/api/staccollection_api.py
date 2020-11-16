# coding: utf-8

"""
    Maxar Content API - Catalog

    The Maxar Content Catalog API implements a STAC-compliant service for searching the Maxar content catalog.  __The STAC specification is still under development.  When version 1.0 of the STAC specification is released the Content Catalog API will be updated to reflect any changes, some of which will not be backward compatible with this current version.__  For information on STAC see [stacspec.org](https://stacspec.org)   # noqa: E501

    OpenAPI spec version: 0.9
    Contact: DL-Content-Catalog@maxar.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from maxarcat_client.api_client import ApiClient


class STACCOLLECTIONApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_audit_search(self, collection_id, **kwargs):  # noqa: E501
        """Search STAC items by audit fields  # noqa: E501

        Retrieve items for a given collectionId by audit fields  For authorization this method requires the use of a valid bearer token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_search(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection_id: Identifier (name) of a specific collection (required)
        :param ModelDatetime audit_insert_date:
        :param ModelDatetime audit_update_date:
        :return: IdList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_audit_search_with_http_info(collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_audit_search_with_http_info(collection_id, **kwargs)  # noqa: E501
            return data

    def get_audit_search_with_http_info(self, collection_id, **kwargs):  # noqa: E501
        """Search STAC items by audit fields  # noqa: E501

        Retrieve items for a given collectionId by audit fields  For authorization this method requires the use of a valid bearer token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audit_search_with_http_info(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection_id: Identifier (name) of a specific collection (required)
        :param ModelDatetime audit_insert_date:
        :param ModelDatetime audit_update_date:
        :return: IdList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id', 'audit_insert_date', 'audit_update_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audit_search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `get_audit_search`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collectionId'] = params['collection_id']  # noqa: E501

        query_params = []
        if 'audit_insert_date' in params:
            query_params.append(('auditInsertDate', params['audit_insert_date']))  # noqa: E501
        if 'audit_update_date' in params:
            query_params.append(('auditUpdateDate', params['audit_update_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionId}/audit', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_collection_stac(self, collection_id, **kwargs):  # noqa: E501
        """Return a collection definition  # noqa: E501

        For authorization this method requires the use of a valid bearer token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_stac(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection_id: Identifier (name) of a specific collection (required)
        :return: Collection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_collection_stac_with_http_info(collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_collection_stac_with_http_info(collection_id, **kwargs)  # noqa: E501
            return data

    def get_collection_stac_with_http_info(self, collection_id, **kwargs):  # noqa: E501
        """Return a collection definition  # noqa: E501

        For authorization this method requires the use of a valid bearer token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_stac_with_http_info(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str collection_id: Identifier (name) of a specific collection (required)
        :return: Collection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_collection_stac" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `get_collection_stac`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collectionId'] = params['collection_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Collection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_collections_stac(self, **kwargs):  # noqa: E501
        """Return all collection definitions  # noqa: E501

        For authorization this method requires the use of a valid bearer token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collections_stac(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Collections
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_collections_stac_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_collections_stac_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_collections_stac_with_http_info(self, **kwargs):  # noqa: E501
        """Return all collection definitions  # noqa: E501

        For authorization this method requires the use of a valid bearer token.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collections_stac_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Collections
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_collections_stac" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/collections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Collections',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)