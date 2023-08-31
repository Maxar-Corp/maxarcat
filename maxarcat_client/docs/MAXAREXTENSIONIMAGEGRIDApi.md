# maxarcat_client.MAXAREXTENSIONIMAGEGRIDApi

All URIs are relative to *https://api.maxar.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_grid**](MAXAREXTENSIONIMAGEGRIDApi.md#get_image_grid) | **GET** /services/imagegrid/search | Search STAC items with filtering and return tiles.
[**get_image_grid_item**](MAXAREXTENSIONIMAGEGRIDApi.md#get_image_grid_item) | **GET** /services/imagegrid/items/{itemId} | Get a gridded tile by its STAC item ID
[**post_image_grid**](MAXAREXTENSIONIMAGEGRIDApi.md#post_image_grid) | **POST** /services/imagegrid/search | Search STAC items with filtering and return tiles.

# **get_image_grid**
> ItemCollection get_image_grid(bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, filter=filter, limit=limit, last=last)

Search STAC items with filtering and return tiles.

Retrieve items matching filters.  For authorization this method requires the use of a valid bearer token.  The GET /service/imagegrid/search operation supports the same search filter parameters as POST /service/imagegrid/search. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONIMAGEGRIDApi(maxarcat_client.ApiClient(configuration))
bbox = 'bbox_example' # str | Bounding box in format \"west,south,east,north\" in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \"bbox\" or \"intersects\", but not both.  (optional)
search_datetime = 'search_datetime_example' # str | Date range filter in format \"start-date/end-date\" or \"exact-datetime\" (optional)
ids = 'ids_example' # str | Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  (optional)
collections = 'collections_example' # str | Comma-separated list of collections to search in.  By default all imagery collections are searched.  It is an error if any collection in this list is not an imagery collection.  (optional)
intersects = 'intersects_example' # str | GeoJSON geometry to search by.  Must be either a Polygon or MultiPolygon geometry.  Only STAC items whose geometries intersect this geometry are selected.  When performing a spatial search specify either of the parameters \"bbox\" or \"intersects\", but not both.  (optional)
filter = 'filter_example' # str | A cql2-text filter expression for filtering items. You can filter on any property inside a STAC item's \"properties\" object.  While STAC items have a \"datetime\" property you should use the search operation's \"datetime\" parameter for searching by it, and not use the \"filter\" parameter for searching by datetime.  (optional)
limit = 56 # int | Maximum number of items to return (optional)
last = 'last_example' # str | STAC item ID of last tile returned in previous page.  Next page of results will begin with tile after this one.  (optional)

try:
    # Search STAC items with filtering and return tiles.
    api_response = api_instance.get_image_grid(bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, filter=filter, limit=limit, last=last)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONIMAGEGRIDApi->get_image_grid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bbox** | **str**| Bounding box in format \&quot;west,south,east,north\&quot; in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \&quot;bbox\&quot; or \&quot;intersects\&quot;, but not both.  | [optional] 
 **search_datetime** | **str**| Date range filter in format \&quot;start-date/end-date\&quot; or \&quot;exact-datetime\&quot; | [optional] 
 **ids** | **str**| Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  | [optional] 
 **collections** | **str**| Comma-separated list of collections to search in.  By default all imagery collections are searched.  It is an error if any collection in this list is not an imagery collection.  | [optional] 
 **intersects** | **str**| GeoJSON geometry to search by.  Must be either a Polygon or MultiPolygon geometry.  Only STAC items whose geometries intersect this geometry are selected.  When performing a spatial search specify either of the parameters \&quot;bbox\&quot; or \&quot;intersects\&quot;, but not both.  | [optional] 
 **filter** | **str**| A cql2-text filter expression for filtering items. You can filter on any property inside a STAC item&#x27;s \&quot;properties\&quot; object.  While STAC items have a \&quot;datetime\&quot; property you should use the search operation&#x27;s \&quot;datetime\&quot; parameter for searching by it, and not use the \&quot;filter\&quot; parameter for searching by datetime.  | [optional] 
 **limit** | **int**| Maximum number of items to return | [optional] 
 **last** | **str**| STAC item ID of last tile returned in previous page.  Next page of results will begin with tile after this one.  | [optional] 

### Return type

[**ItemCollection**](ItemCollection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_grid_item**
> Item get_image_grid_item(item_id)

Get a gridded tile by its STAC item ID

For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONIMAGEGRIDApi(maxarcat_client.ApiClient(configuration))
item_id = 'item_id_example' # str | STAC item ID

try:
    # Get a gridded tile by its STAC item ID
    api_response = api_instance.get_image_grid_item(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONIMAGEGRIDApi->get_image_grid_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| STAC item ID | 

### Return type

[**Item**](Item.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image_grid**
> ItemCollectionPost post_image_grid(body=body)

Search STAC items with filtering and return tiles.

Retrieve items matching filters.  For authorization this method requires the use of a valid bearer token.  The GET /service/imagegrid/search operation supports the same search filter parameters as POST /service/imagegrid/search. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONIMAGEGRIDApi(maxarcat_client.ApiClient(configuration))
body = maxarcat_client.SearchBody() # SearchBody |  (optional)

try:
    # Search STAC items with filtering and return tiles.
    api_response = api_instance.post_image_grid(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONIMAGEGRIDApi->post_image_grid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchBody**](SearchBody.md)|  | [optional] 

### Return type

[**ItemCollectionPost**](ItemCollectionPost.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

