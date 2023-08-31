# maxarcat_client.STACCOLLECTIONApi

All URIs are relative to *https://api.maxar.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_search**](STACCOLLECTIONApi.md#get_audit_search) | **GET** /collections/{collectionId}/audit | Search STAC items by audit fields
[**get_collection_queryables_stac**](STACCOLLECTIONApi.md#get_collection_queryables_stac) | **GET** /collections/{collectionId}/queryables | Queryables for Discovery API
[**get_collection_stac**](STACCOLLECTIONApi.md#get_collection_stac) | **GET** /collections/{collectionId} | Return a collection definition
[**get_collections_stac**](STACCOLLECTIONApi.md#get_collections_stac) | **GET** /collections | Return collection definitions

# **get_audit_search**
> IdList get_audit_search(collection_id, audit_insert_date=audit_insert_date, audit_update_date=audit_update_date, orderby=orderby, sortby=sortby, limit=limit, page=page)

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
orderby = 'ASC' # str | Will be deprecated in favor of the `sortby` parameter.  You can only define one or the other. You can choose to order by ASC or DESC, with the default being ASC  (optional) (default to ASC)
sortby = 'ASC' # str | You can choose to order by ASC or DESC, with the default being ASC  (optional) (default to ASC)
limit = 1000 # int | Maximum number of ids to return (default of 1000) (optional) (default to 1000)
page = 1 # int | Page number to retrieve.  First page is numbered 1.  (optional) (default to 1)

try:
    # Search STAC items by audit fields
    api_response = api_instance.get_audit_search(collection_id, audit_insert_date=audit_insert_date, audit_update_date=audit_update_date, orderby=orderby, sortby=sortby, limit=limit, page=page)
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
 **orderby** | **str**| Will be deprecated in favor of the &#x60;sortby&#x60; parameter.  You can only define one or the other. You can choose to order by ASC or DESC, with the default being ASC  | [optional] [default to ASC]
 **sortby** | **str**| You can choose to order by ASC or DESC, with the default being ASC  | [optional] [default to ASC]
 **limit** | **int**| Maximum number of ids to return (default of 1000) | [optional] [default to 1000]
 **page** | **int**| Page number to retrieve.  First page is numbered 1.  | [optional] [default to 1]

### Return type

[**IdList**](IdList.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_queryables_stac**
> Queryables get_collection_queryables_stac(collection_id)

Queryables for Discovery API

Queryable names for the Discovery API Item Search filter.  For authorization this method requires the use of a valid bearer token. 

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
    # Queryables for Discovery API
    api_response = api_instance.get_collection_queryables_stac(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACCOLLECTIONApi->get_collection_queryables_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 

### Return type

[**Queryables**](Queryables.md)

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
> Collections get_collections_stac(sortby=sortby, limit=limit, page=page)

Return collection definitions

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
sortby = 'sortby_example' # str | An array of property names, prefixed by either \"+\" for ascending or \"-\" for descending. If no prefix is provided, \"+\" is assumed. Currently only two properties are supported: `datetime` and `id`.  (optional)
limit = 56 # int | Maximum number of collections to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # Return collection definitions
    api_response = api_instance.get_collections_stac(sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACCOLLECTIONApi->get_collections_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortby** | **str**| An array of property names, prefixed by either \&quot;+\&quot; for ascending or \&quot;-\&quot; for descending. If no prefix is provided, \&quot;+\&quot; is assumed. Currently only two properties are supported: &#x60;datetime&#x60; and &#x60;id&#x60;.  | [optional] 
 **limit** | **int**| Maximum number of collections to return | [optional] 
 **page** | **int**| Page number to retrieve.  First page is numbered 1.  | [optional] 

### Return type

[**Collections**](Collections.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

