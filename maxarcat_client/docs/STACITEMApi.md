# maxarcat_client.STACITEMApi

All URIs are relative to *https://api.maxar.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_item_stac**](STACITEMApi.md#get_item_stac) | **GET** /collections/{collectionId}/items/{itemId} | Get STAC item
[**get_items_stac**](STACITEMApi.md#get_items_stac) | **GET** /collections/{collectionId}/items | Search STAC items in a collection.

# **get_item_stac**
> Item get_item_stac(collection_id, item_id)

Get STAC item

For authorization this method requires the use of a valid bearer token.

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACITEMApi(maxarcat_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection
item_id = 'item_id_example' # str | STAC item ID

try:
    # Get STAC item
    api_response = api_instance.get_item_stac(collection_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACITEMApi->get_item_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 
 **item_id** | **str**| STAC item ID | 

### Return type

[**Item**](Item.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_stac**
> ItemCollection get_items_stac(collection_id, bbox=bbox, search_datetime=search_datetime, ids=ids, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)

Search STAC items in a collection.

The same query parameters may be used as those in the /search endpoint, except for \"collections\" since the collection to search is part of the URL path.  For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACITEMApi(maxarcat_client.ApiClient(configuration))
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection
bbox = 'bbox_example' # str | Bounding box in format \"west,south,east,north\" in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
search_datetime = 'search_datetime_example' # str | Date range filter in format \"start-date/end-date\" or \"exact-datetime\" (optional)
ids = 'ids_example' # str | Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  (optional)
intersects = 'intersects_example' # str | GeoJSON geometry to search by.  Only STAC items whose geometries intersect this geometry are selected. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
filter = 'filter_example' # str | A cql2-text filter expression for filtering items. You can filter on any property inside a STAC item's \"properties\" object.  While STAC items have a \"datetime\" property you should use the search operation's \"datetime\" parameter for searching by it, and not use the \"filter\" parameter for searching by datetime.  (optional)
sortby = 'sortby_example' # str | An array of property names, prefixed by either \"+\" for ascending or \"-\" for descending. If no prefix is provided, \"+\" is assumed.  (optional)
limit = 56 # int | Maximum number of items to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # Search STAC items in a collection.
    api_response = api_instance.get_items_stac(collection_id, bbox=bbox, search_datetime=search_datetime, ids=ids, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACITEMApi->get_items_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **str**| Identifier (name) of a specific collection | 
 **bbox** | **str**| Bounding box in format \&quot;west,south,east,north\&quot; in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \&quot;bbox\&quot; of \&quot;intesects\&quot;, but not both.  | [optional] 
 **search_datetime** | **str**| Date range filter in format \&quot;start-date/end-date\&quot; or \&quot;exact-datetime\&quot; | [optional] 
 **ids** | **str**| Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  | [optional] 
 **intersects** | **str**| GeoJSON geometry to search by.  Only STAC items whose geometries intersect this geometry are selected. When performing a spatial search specify either of the parameters \&quot;bbox\&quot; of \&quot;intesects\&quot;, but not both.  | [optional] 
 **filter** | **str**| A cql2-text filter expression for filtering items. You can filter on any property inside a STAC item&#x27;s \&quot;properties\&quot; object.  While STAC items have a \&quot;datetime\&quot; property you should use the search operation&#x27;s \&quot;datetime\&quot; parameter for searching by it, and not use the \&quot;filter\&quot; parameter for searching by datetime.  | [optional] 
 **sortby** | **str**| An array of property names, prefixed by either \&quot;+\&quot; for ascending or \&quot;-\&quot; for descending. If no prefix is provided, \&quot;+\&quot; is assumed.  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] 
 **page** | **int**| Page number to retrieve.  First page is numbered 1.  | [optional] 

### Return type

[**ItemCollection**](ItemCollection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

