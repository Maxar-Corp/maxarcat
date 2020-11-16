# maxarcat_client.STACCOLLECTIONApi

All URIs are relative to *https://beta-api.content.satcloud.us/catalog*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_search**](STACCOLLECTIONApi.md#get_audit_search) | **GET** /collections/{collectionId}/audit | Search STAC items by audit fields
[**get_collection_stac**](STACCOLLECTIONApi.md#get_collection_stac) | **GET** /collections/{collectionId} | Return a collection definition
[**get_collections_stac**](STACCOLLECTIONApi.md#get_collections_stac) | **GET** /collections | Return all collection definitions

# **get_audit_search**
> IdList get_audit_search(collection_id, audit_insert_date=audit_insert_date, audit_update_date=audit_update_date)

Search STAC items by audit fields

Retrieve items for a given collectionId by audit fields  For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACCOLLECTIONApi(maxarcat_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection
audit_insert_date = maxarcat_client.ModelDatetime() # ModelDatetime |  (optional)
audit_update_date = maxarcat_client.ModelDatetime() # ModelDatetime |  (optional)

try:
    # Search STAC items by audit fields
    api_response = api_instance.get_audit_search(collection_id, audit_insert_date=audit_insert_date, audit_update_date=audit_update_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACCOLLECTIONApi->get_audit_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 
 **audit_insert_date** | [**ModelDatetime**](.md)|  | [optional] 
 **audit_update_date** | [**ModelDatetime**](.md)|  | [optional] 

### Return type

[**IdList**](IdList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_stac**
> Collection get_collection_stac(collection_id)

Return a collection definition

For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACCOLLECTIONApi(maxarcat_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection

try:
    # Return a collection definition
    api_response = api_instance.get_collection_stac(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACCOLLECTIONApi->get_collection_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections_stac**
> Collections get_collections_stac()

Return all collection definitions

For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACCOLLECTIONApi(maxarcat_client.ApiClient(configuration))

try:
    # Return all collection definitions
    api_response = api_instance.get_collections_stac()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACCOLLECTIONApi->get_collections_stac: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Collections**](Collections.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

