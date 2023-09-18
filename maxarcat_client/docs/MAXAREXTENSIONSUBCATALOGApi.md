# maxarcat_client.MAXAREXTENSIONSUBCATALOGApi

All URIs are relative to *https://api.maxar.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sub_catalog**](MAXAREXTENSIONSUBCATALOGApi.md#get_sub_catalog) | **GET** /catalogs/{subCatalogId} | Get sub-catalog definition
[**get_sub_catalog_collection**](MAXAREXTENSIONSUBCATALOGApi.md#get_sub_catalog_collection) | **GET** /catalogs/{subCatalogId}/collections/{collectionId} | Get Collection in a Sub-Catalog
[**get_sub_catalog_item**](MAXAREXTENSIONSUBCATALOGApi.md#get_sub_catalog_item) | **GET** /catalogs/{subCatalogId}/collections/{collectionId}/items/{itemId} | Get Sub-Catalog STAC Item
[**get_sub_catalog_search**](MAXAREXTENSIONSUBCATALOGApi.md#get_sub_catalog_search) | **GET** /catalogs/{subCatalogId}/search | Search Sub-Catalog STAC items with filtering.
[**list_sub_catalog_collection_items**](MAXAREXTENSIONSUBCATALOGApi.md#list_sub_catalog_collection_items) | **GET** /catalogs/{subCatalogId}/collections/{collectionId}/items | List Items in a Sub-Catalog&#x27;s collection
[**list_sub_catalog_collections**](MAXAREXTENSIONSUBCATALOGApi.md#list_sub_catalog_collections) | **GET** /catalogs/{subCatalogId}/collections | List Sub-Catalog Collections
[**list_sub_catalogs**](MAXAREXTENSIONSUBCATALOGApi.md#list_sub_catalogs) | **GET** /catalogs | List top level Maxar Sub-Catalogs
[**post_sub_catalog_search**](MAXAREXTENSIONSUBCATALOGApi.md#post_sub_catalog_search) | **POST** /catalogs/{subCatalogId}/search | Search Sub-Catalog STAC items with filtering.

# **get_sub_catalog**
> Collection get_sub_catalog(sub_catalog_id)

Get sub-catalog definition

View the definition of a Maxar Sub-Catalog 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection

try:
    # Get sub-catalog definition
    api_response = api_instance.get_sub_catalog(sub_catalog_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->get_sub_catalog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_catalog_collection**
> Collection get_sub_catalog_collection(sub_catalog_id, collection_id)

Get Collection in a Sub-Catalog

View the definition of a collection that belongs to a Sub-Catalog 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection

try:
    # Get Collection in a Sub-Catalog
    api_response = api_instance.get_sub_catalog_collection(sub_catalog_id, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->get_sub_catalog_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 
 **collection_id** | **str**| Identifier (name) of a specific collection | 

### Return type

[**Collection**](Collection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_catalog_item**
> Item get_sub_catalog_item(sub_catalog_id, collection_id, item_id)

Get Sub-Catalog STAC Item

Get a stac item in a sub-catalog's collection

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection
collection_id = 'collection_id_example' # str | Identifier (name) of a specific collection
item_id = 'item_id_example' # str | STAC item ID

try:
    # Get Sub-Catalog STAC Item
    api_response = api_instance.get_sub_catalog_item(sub_catalog_id, collection_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->get_sub_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 
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

# **get_sub_catalog_search**
> ItemCollection get_sub_catalog_search(sub_catalog_id, bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)

Search Sub-Catalog STAC items with filtering.

Retrieve items matching filters in a sub-catalog. The GET /search operation supports the same search filter parameters as POST /search. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection
bbox = 'bbox_example' # str | Bounding box in format \"west,south,east,north\" in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
search_datetime = 'search_datetime_example' # str | Date range filter in format \"start-date/end-date\" or \"exact-datetime\" (optional)
ids = 'ids_example' # str | Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  (optional)
collections = 'collections_example' # str | Comma-separated list of collections to search in.  If this parameter is not specified then items in all collections are searched.  (optional)
intersects = 'intersects_example' # str | GeoJSON geometry to search by.  Only STAC items whose geometries intersect this geometry are selected. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
filter = 'filter_example' # str | A cql2-text filter expression for filtering items. You can filter on any property inside a STAC item's \"properties\" object.  While STAC items have a \"datetime\" property you should use the search operation's \"datetime\" parameter for searching by it, and not use the \"filter\" parameter for searching by datetime.  (optional)
sortby = 'sortby_example' # str | An array of property names, prefixed by either \"+\" for ascending or \"-\" for descending. If no prefix is provided, \"+\" is assumed.  (optional)
limit = 56 # int | Maximum number of items to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # Search Sub-Catalog STAC items with filtering.
    api_response = api_instance.get_sub_catalog_search(sub_catalog_id, bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->get_sub_catalog_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 
 **bbox** | **str**| Bounding box in format \&quot;west,south,east,north\&quot; in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \&quot;bbox\&quot; of \&quot;intesects\&quot;, but not both.  | [optional] 
 **search_datetime** | **str**| Date range filter in format \&quot;start-date/end-date\&quot; or \&quot;exact-datetime\&quot; | [optional] 
 **ids** | **str**| Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  | [optional] 
 **collections** | **str**| Comma-separated list of collections to search in.  If this parameter is not specified then items in all collections are searched.  | [optional] 
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
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sub_catalog_collection_items**
> ItemCollection list_sub_catalog_collection_items(sub_catalog_id, collection_id, bbox=bbox, search_datetime=search_datetime, ids=ids, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)

List Items in a Sub-Catalog's collection

List items that are in a collection. The same query parameters may be used as those in the /search endpoint, except for \"collections\" since the collection to search is part of the URL path. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection
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
    # List Items in a Sub-Catalog's collection
    api_response = api_instance.list_sub_catalog_collection_items(sub_catalog_id, collection_id, bbox=bbox, search_datetime=search_datetime, ids=ids, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->list_sub_catalog_collection_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 
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

# **list_sub_catalog_collections**
> Collections list_sub_catalog_collections(sub_catalog_id, sortby=sortby, limit=limit, page=page)

List Sub-Catalog Collections

List the collections that belong to a Sub-Catalog 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection
sortby = 'sortby_example' # str | An array of property names, prefixed by either \"+\" for ascending or \"-\" for descending. If no prefix is provided, \"+\" is assumed.  (optional)
limit = 56 # int | Maximum number of collections to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # List Sub-Catalog Collections
    api_response = api_instance.list_sub_catalog_collections(sub_catalog_id, sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->list_sub_catalog_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 
 **sortby** | **str**| An array of property names, prefixed by either \&quot;+\&quot; for ascending or \&quot;-\&quot; for descending. If no prefix is provided, \&quot;+\&quot; is assumed.  | [optional] 
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

# **list_sub_catalogs**
> Collections list_sub_catalogs(sortby=sortby, limit=limit, page=page)

List top level Maxar Sub-Catalogs

View the available Maxar Sub-Catalogs that can be navigated as a self-contained STAC catalog 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sortby = 'sortby_example' # str | An array of property names, prefixed by either \"+\" for ascending or \"-\" for descending. If no prefix is provided, \"+\" is assumed.  (optional)
limit = 56 # int | Maximum number of collections to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # List top level Maxar Sub-Catalogs
    api_response = api_instance.list_sub_catalogs(sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->list_sub_catalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortby** | **str**| An array of property names, prefixed by either \&quot;+\&quot; for ascending or \&quot;-\&quot; for descending. If no prefix is provided, \&quot;+\&quot; is assumed.  | [optional] 
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

# **post_sub_catalog_search**
> ItemCollectionPost post_sub_catalog_search(sub_catalog_id, body=body)

Search Sub-Catalog STAC items with filtering.

Retrieve items matching filters in a sub-catalog. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.MAXAREXTENSIONSUBCATALOGApi(maxarcat_client.ApiClient(configuration))
sub_catalog_id = 'sub_catalog_id_example' # str | Identifier (name) of a specific collection
body = maxarcat_client.SearchBody() # SearchBody |  (optional)

try:
    # Search Sub-Catalog STAC items with filtering.
    api_response = api_instance.post_sub_catalog_search(sub_catalog_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MAXAREXTENSIONSUBCATALOGApi->post_sub_catalog_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_catalog_id** | **str**| Identifier (name) of a specific collection | 
 **body** | [**SearchBody**](SearchBody.md)|  | [optional] 

### Return type

[**ItemCollectionPost**](ItemCollectionPost.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

