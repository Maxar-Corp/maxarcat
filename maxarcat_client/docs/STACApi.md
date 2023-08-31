# maxarcat_client.STACApi

All URIs are relative to *https://api.maxar.com/discovery/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_conformance**](STACApi.md#get_conformance) | **GET** /conformance | Information about specifications that this API conforms to
[**get_healthcheck**](STACApi.md#get_healthcheck) | **GET** /healthcheck | Service healthcheck
[**get_queryables_stac**](STACApi.md#get_queryables_stac) | **GET** /queryables | Queryables for Discovery API
[**get_root**](STACApi.md#get_root) | **GET** / | Return the root catalog or collection.
[**get_search_stac**](STACApi.md#get_search_stac) | **GET** /search | Search STAC items with filtering.
[**get_status**](STACApi.md#get_status) | **GET** /status | Service status
[**post_search_stac**](STACApi.md#post_search_stac) | **POST** /search | Search STAC items with filtering.
[**validate_stac_object**](STACApi.md#validate_stac_object) | **POST** /validate | Validate a STAC object

# **get_conformance**
> ServerConformance get_conformance()

Information about specifications that this API conforms to

A list of all conformance classes specified in a standard that the server conforms to. 

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
    # Information about specifications that this API conforms to
    api_response = api_instance.get_conformance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_conformance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerConformance**](ServerConformance.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **get_queryables_stac**
> Queryables get_queryables_stac()

Queryables for Discovery API

Queryables for the Discovery API Item Search filter.  For authorization this method requires the use of a valid bearer token. 

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
    # Queryables for Discovery API
    api_response = api_instance.get_queryables_stac()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_queryables_stac: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Queryables**](Queryables.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_root**
> LandingPage get_root()

Return the root catalog or collection.

Returns the root STAC Catalog that is the entry point for users to browse with STAC Browser or for search engines to crawl. 

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
> ItemCollection get_search_stac(bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)

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
search_datetime = 'search_datetime_example' # str | Date range filter in format \"start-date/end-date\" or \"exact-datetime\" (optional)
ids = 'ids_example' # str | Comma-separated list of STAC item IDs to return.  The items returned are still subject to whatever other search filters are specified.  (optional)
collections = 'collections_example' # str | Comma-separated list of collections to search in.  If this parameter is not specified then items in all collections are searched.  (optional)
intersects = 'intersects_example' # str | GeoJSON geometry to search by.  Only STAC items whose geometries intersect this geometry are selected. When performing a spatial search specify either of the parameters \"bbox\" of \"intesects\", but not both.  (optional)
filter = 'filter_example' # str | A cql2-text filter expression for filtering items. You can filter on any property inside a STAC item's \"properties\" object.  While STAC items have a \"datetime\" property you should use the search operation's \"datetime\" parameter for searching by it, and not use the \"filter\" parameter for searching by datetime.  (optional)
sortby = 'sortby_example' # str | An array of property names, prefixed by either \"+\" for ascending or \"-\" for descending. If no prefix is provided, \"+\" is assumed.  (optional)
limit = 56 # int | Maximum number of items to return (optional)
page = 56 # int | Page number to retrieve.  First page is numbered 1.  (optional)

try:
    # Search STAC items with filtering.
    api_response = api_instance.get_search_stac(bbox=bbox, search_datetime=search_datetime, ids=ids, collections=collections, intersects=intersects, filter=filter, sortby=sortby, limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_search_stac: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_status**
> Status get_status()

Service status

Return the service's status.  For authorization this method requires the use of a valid bearer token. 

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
    # Service status
    api_response = api_instance.get_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->get_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_search_stac**
> ItemCollectionPost post_search_stac(body=body)

Search STAC items with filtering.

Retrieve items matching filters.  For authorization this method requires the use of a valid bearer token. 

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
    # Search STAC items with filtering.
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

[**ItemCollectionPost**](ItemCollectionPost.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/geo+json, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_stac_object**
> ValidationResult validate_stac_object()

Validate a STAC object

Post an object to validate it against its respective stac type. E.g. catalog, collection, item. 

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
    # Validate a STAC object
    api_response = api_instance.validate_stac_object()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling STACApi->validate_stac_object: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ValidationResult**](ValidationResult.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

