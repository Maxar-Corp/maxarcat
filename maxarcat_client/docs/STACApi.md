# maxarcat_client.STACApi

All URIs are relative to *https://beta-api.content.satcloud.us/catalog*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_healthcheck**](STACApi.md#get_healthcheck) | **GET** /healthcheck | Service healthcheck
[**get_root**](STACApi.md#get_root) | **GET** / | Return the root catalog or collection.
[**get_search_stac**](STACApi.md#get_search_stac) | **GET** /search | Search STAC items with filtering.
[**post_search_stac**](STACApi.md#post_search_stac) | **POST** /search | Search STAC items with full-featured filtering.

# **get_healthcheck**
> Healthcheck get_healthcheck()

Service healthcheck

Return the service's health and the health of each of its dependent services.  For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACApi(maxarcat_client.ApiClient(configuration))

try:
    # Service healthcheck
    api_response = api_instance.get_healthcheck()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_healthcheck: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Healthcheck**](Healthcheck.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> LandingPage get_root()

Return the root catalog or collection.

This method is currently unimplemented.  It returns status 200 with JSON content of an empty dictionary.  Returns the root STAC Catalog or STAC Collection that is the entry point for users to browse with STAC Browser or for search engines to crawl. This can either return a single STAC Collection or more commonly a STAC catalog that usually lists sub-catalogs of STAC Collections, i.e. a simple catalog that lists all collections available through the API. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACApi(maxarcat_client.ApiClient(configuration))

try:
    # Return the root catalog or collection.
    api_response = api_instance.get_root()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_root: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LandingPage**](LandingPage.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_stac**
> ItemCollection get_search_stac(bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, where=where, orderby=orderby, limit=limit, page=page)

Search STAC items with filtering.

Retrieve items matching filters.  For authorization this method requires the use of a valid bearer token.  The GET /search operation supports the same search filter parameters as POST /search. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACApi(maxarcat_client.ApiClient(configuration))
bbox = 'bbox_example' # str | Bounding box in format \"west,south,east,north\" in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
search_datetime = 'search_datetime_example' # str | Date range filter in format \"start-date/end-date\" (optional)
ids = 'ids_example' # str | Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  (optional)
collections = 'collections_example' # str | Comma-separated list of collections to search in.  If this parameter is not specified then items in all collections are searched.  (optional)
intersects = 'intersects_example' # str | GeoJSON geometry to search by.  Only STAC items whose geometries intersect this geometry are selected. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
where = 'where_example' # str | SQL-style WHERE clause for filtering STAC items by properties.  You can filter on any property inside a STAC item's \"properties\" object.  While STAC items have a \"datetime\" property you should use the search operation's \"datetime\" parameter for searching by it, and not use the \"where\" parameter for searching by datetime.  (optional)
orderby = 'orderby_example' # str | SQL-style ORDER BY clause.  The only properties results can be ordered by are \"id\" and \"datetime\". You can use ASC and DESC modifiers on each column.  If not specified then orderby defaults to \"datetime DESC, id ASC\".  (optional)
limit = 56 # int | Maximum number of items to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # Search STAC items with filtering.
    api_response = api_instance.get_search_stac(bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, where=where, orderby=orderby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_search_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bbox** | **str**| Bounding box in format \&quot;west,south,east,north\&quot; in WGS84 decimal degrees. When performing a spatial search specify either of the parameters \&quot;bbox\&quot; of \&quot;intesects\&quot;, but not both.  | [optional] 
 **search_datetime** | **str**| Date range filter in format \&quot;start-date/end-date\&quot; | [optional] 
 **ids** | **str**| Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  | [optional] 
 **collections** | **str**| Comma-separated list of collections to search in.  If this parameter is not specified then items in all collections are searched.  | [optional] 
 **intersects** | **str**| GeoJSON geometry to search by.  Only STAC items whose geometries intersect this geometry are selected. When performing a spatial search specify either of the parameters \&quot;bbox\&quot; of \&quot;intesects\&quot;, but not both.  | [optional] 
 **where** | **str**| SQL-style WHERE clause for filtering STAC items by properties.  You can filter on any property inside a STAC item&#x27;s \&quot;properties\&quot; object.  While STAC items have a \&quot;datetime\&quot; property you should use the search operation&#x27;s \&quot;datetime\&quot; parameter for searching by it, and not use the \&quot;where\&quot; parameter for searching by datetime.  | [optional] 
 **orderby** | **str**| SQL-style ORDER BY clause.  The only properties results can be ordered by are \&quot;id\&quot; and \&quot;datetime\&quot;. You can use ASC and DESC modifiers on each column.  If not specified then orderby defaults to \&quot;datetime DESC, id ASC\&quot;.  | [optional] 
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

# **post_search_stac**
> ItemCollection post_search_stac(body=body)

Search STAC items with full-featured filtering.

Retrieve items matching filters. Intended as the standard, full-featured query API.  For authorization this method requires the use of a valid bearer token. 

### Example
```python
from __future__ import print_function
import time
import maxarcat_client
from maxarcat_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = maxarcat_client.STACApi(maxarcat_client.ApiClient(configuration))
body = maxarcat_client.SearchBody() # SearchBody |  (optional)

try:
    # Search STAC items with full-featured filtering.
    api_response = api_instance.post_search_stac(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->post_search_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchBody**](SearchBody.md)|  | [optional] 

### Return type

[**ItemCollection**](ItemCollection.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

