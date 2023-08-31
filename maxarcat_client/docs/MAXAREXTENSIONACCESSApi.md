# maxarcat_client.MAXAREXTENSIONACCESSApi

All URIs are relative to *https://api.maxar.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_collection_dap**](MAXAREXTENSIONACCESSApi.md#get_collection_dap) | **GET** /collections/{collectionId}/dap | Get Collection DAP
[**get_item_dap**](MAXAREXTENSIONACCESSApi.md#get_item_dap) | **GET** /collections/{collectionId}/items/{itemId}/dap | Get Data Access Profile for an Item

# **get_collection_dap**
> CollectionDataAccessProfile get_collection_dap(collection_id)

Get Collection DAP

Retrieve the Data Access Profile for a Collection by ID

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONACCESSApi(maxarcat_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection

try:
    # Get Collection DAP
    api_response = api_instance.get_collection_dap(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONACCESSApi->get_collection_dap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 

### Return type

[**CollectionDataAccessProfile**](CollectionDataAccessProfile.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_dap**
> DataAccessProfile get_item_dap(collection_id, item_id)

Get Data Access Profile for an Item

Strictly for internal use, this endpoint retrieves the whole data access profile for an item in a collection

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONACCESSApi(maxarcat_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection
item_id = 'item_id_example' # str | STAC item ID

try:
    # Get Data Access Profile for an Item
    api_response = api_instance.get_item_dap(collection_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONACCESSApi->get_item_dap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 
 **item_id** | **str**| STAC item ID | 

### Return type

[**DataAccessProfile**](DataAccessProfile.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

