#
# catalog.py
#
# Maxar catalog Python client.
#

import collections.abc as abc
import getpass
import json
import logging
from contextlib import contextmanager
from datetime import datetime
from typing import Optional, Tuple, Union

import requests

import maxarcat_client
import maxarcat_client.rest
from maxarcat.exceptions import CatalogError


class Catalog:
    default_catalog_url = 'https://api.content.maxar.com/catalog'

    default_auth_url = 'https://auth.content.maxar.com/v1/oauth2/token'

    # Class-level logger shared by all Catalog instances
    logger_name = 'maxar.catalog'
    logger = logging.getLogger(logger_name)

    def __init__(self, token: str, url: str = None):
        """
        Initialize connection to Maxar catalog using the given Content Hub token.

        A Catalog object does not generate a new token once its current token has expired.
        It is the user's responsibility to create a new Catalog object if a token expires
        and a new one needs to be generated.

        :param url: URL of Catalog service.  If None then use default URL.
        :param token: Content Hub token to use in service requests.
        :param verbose: If True then Catalog methods print informational messages to stdout.
        """
        self._token = token
        self.url = url if url else self.default_catalog_url
        self.last_response = None

        # Setup the swagger clients
        self._stac_api = self._setup_api(maxarcat_client.STACApi())
        self._coll_api = self._setup_api(maxarcat_client.STACCOLLECTIONApi())
        self._item_api = self._setup_api(maxarcat_client.STACITEMApi())

    def _setup_api(self, api):
        # Hack to get auth to work.  I'm not sure how to setup auth for the swagger
        # client with bearer token correctly.
        api.api_client.default_headers['Authorization'] = f'Bearer {self._token}'
        # Override the default endpoint in the OpenAPI spec
        api.api_client.configuration.host = self.url
        return api

    @staticmethod
    @contextmanager
    def timer():
        """
        Context manager that times its block and logs a message about elapsed time afterwards.
        """
        start_time = datetime.now()
        try:
            yield
        finally:
            elapsed = datetime.now() - start_time
            Catalog.logger.info('Elapsed seconds: {0:.2f}'.format(elapsed.total_seconds()))

    @staticmethod
    def connect(username: str = None, password: str = None, **kwargs):
        """
        Construct and return a Catalog using a Content Hub token generated from the given
        credentials.  Prompt the user to input username and password if they are not provided.
        :param username: Content Hub username
        :param password: Content Hub password
        :param kwargs: Additional keyword args to pass to Catalog constructor
        :return: New Catalog
        """
        if not username and password:
            raise CatalogError('Cannot specify password without username')
        if not username:
            username = input('Username: ')
        if not password:
            password = getpass.getpass('Password: ')
        token = Catalog.get_token(Catalog.default_auth_url, username, password)
        del password
        return Catalog(token, **kwargs)

    @staticmethod
    def get_token(auth_url: str, username: str, password: str = None) -> str:
        """
        Generate a token from the Content Hub authorization service.

        :param auth_url: URL to authorization service, generally "https://auth.content.maxar.com/v1/oauth2/token"
        :param username: Content Hub username.
        :param password: Content Hub password.
        :return: Content Hub token.
        :raises CatalogError: if user is unauthorized, or any other kind of error generating token.
        """

        # Content Hub auth service successful response with status 200:
        # {
        #     'token_type': 'Bearer', 
        #     'expires_in': 43200, 
        #     'access_token': 'eyJraWQiOiJRcENwTVNyUFJGSDNBbk...', 
        #     'scope': 'content.rda.use content.internal content.catalog.use'
        # }

        Catalog.logger.info(f'Requesting token from {auth_url}')
        response = requests.post(auth_url, auth=(username, password))
        try:
            body = json.loads(response.text)
        except Exception as exp:
            raise CatalogError(
                'Error requesting Content Hub token.  Response from Content Hub authorization service is not JSON.') from exp
        token = body.get('access_token')
        if token:
            Catalog.logger.info('Token successfully received.')
            return token
        error = body.get('Error')
        if error:
            raise CatalogError(f'Error requesting Content Hub token: {error}')
        raise CatalogError(
            f'Error requesting Content Hub token.  Unexpected response from service: {body}')

    def get_healthcheck(self) -> maxarcat_client.models.Healthcheck:
        """
        Call the Catalog API healthcheck method
        :return: Healthcheck
        """
        return self._call_api(
            self._stac_api.get_healthcheck_with_http_info)

    def get_collection(self, collection_id=None) -> Union[maxarcat_client.models.Collection, None]:
        """
        Get a collection by its ID.

        :param collection_id: Collection to get.
        :raises CatalogError: On error during request.
        :return: Collection model, or None if collection does not exist.
        """
        if not collection_id:
            raise CatalogError('Required parameter collection_id is empty')
        Catalog.logger.info(f'Get collection {collection_id}')
        try:
            return self._call_api(
                self._coll_api.get_collection_stac_with_http_info, collection_id=collection_id)
        except CatalogError as exp:
            if exp.status == 404:
                return None
            raise

    def get_collections(self) -> maxarcat_client.models.Collections:
        """
        Return all collections in the Maxar Catalog.
        :return: Collections model.
        """
        Catalog.logger.info('Get all collections')
        return self._call_api(self._coll_api.get_collections_stac_with_http_info)

    def get_item(self, item_id: str, collection_id: str = None) -> Union[maxarcat_client.models.Item, None]:
        """
        Return a single item given its ID.

        :param item_id: Item ID
        :param collection_id: Optional collection ID
        :return: Item if it exists, else None.
        """
        if not item_id:
            raise CatalogError('Required parameter item_id is empty.')

        if collection_id:
            Catalog.logger.info(f'Get item {item_id} in collection {collection_id}')
            try:
                return self._call_api(self._item_api.get_item_stac_with_http_info,
                                      collection_id=collection_id, item_id=item_id)
            except CatalogError as exp:
                if exp.status == 404:
                    return None
                raise

        Catalog.logger.info(f'Get item {item_id}')
        response: maxarcat_client.models.ItemCollection = self._call_api(
            self._stac_api.get_search_stac_with_http_info, ids=item_id)
        if response.features:
            return response.features[0]
        else:
            return None

    def search(self, collections: list = None, bbox: list = None, intersects: dict = None,
               start_datetime: datetime = None, end_datetime: datetime = None,
               item_ids: list = None, where: str = None, orderby: str = None,
               limit: int = None, page: int = None,
               complete: bool = None) -> maxarcat_client.models.ItemCollection:
        """
        Query the Maxar catalog.

        :param collections: A list of collections to query against
        :param bbox: Bounding box in degrees to search by.  Format is a sequence of the form [west, south, east, north]
            or [west, south, zmin, east, north, zmax].  Optional.
        :param intersects: Geometry to search by.  Dict of GeoJSON.  Optional.
        :param start_datetime:
        :param end_datetime:
        :param item_ids: List of item IDs to query.
        :param where: STAC item properties filter.
        :param orderby: Columns to order result by.
        :param limit: Maximum number of items to return.
        :param page: Page number to return, starting at 1.
        :param complete: If False then include incomplete features in the search.  These are features
            added to the catalog but with incomplete metadata.  Most users should only request complete features.
        :return: GeoJSON FeatureCollection as dict
        """

        body = {}
        if collections:
            body['collections'] = collections
            Catalog.logger.info(f'Search collections: {collections}')
        if bbox:
            body['bbox'] = bbox
            Catalog.logger.info(f'Search bbox: {bbox}')
        if intersects:
            body['intersects'] = intersects
            Catalog.logger.info('Search geometry: {} ...'.format(json.dumps(intersects)[:100]))

        # Handle date range
        date_range = None
        if start_datetime and end_datetime:
            date_range = '{}/{}'.format(
                Catalog.format_datetime_iso8601(start_datetime),
                Catalog.format_datetime_iso8601(end_datetime))
        elif start_datetime:
            date_range = '{}/..'.format(Catalog.format_datetime_iso8601(start_datetime))
        elif end_datetime:
            date_range = '../{}'.format(Catalog.format_datetime_iso8601(end_datetime))
        if date_range:
            body['datetime'] = date_range
            Catalog.logger.info(f'Search time range: {date_range}')

        if item_ids:
            # Guard against a single image ID being passed in, which as a string would be interpreted as a sequence.
            if not isinstance(item_ids, abc.Sequence):
                raise CatalogError('item_ids must be a sequence')
            body['ids'] = list(item_ids)

        if where:
            body['where'] = where
            Catalog.logger.info(f'Search where: {where}')
        if orderby:
            body['orderby'] = orderby
            Catalog.logger.info(f'Search order by: {orderby}')
        if limit:
            body['limit'] = limit
            Catalog.logger.info(f'Search limit: {limit}')
        if page:
            body['page'] = page
            Catalog.logger.info(f'Search page: {page}')
        if complete is not None:
            complete_value = True if complete else False
            body['complete'] = complete_value
            Catalog.logger.info(f'Complete: {complete_value}')

        return self._call_api(self._stac_api.post_search_stac_with_http_info, body=body)

    def query(self, collections: list = None, bbox: list = None, intersects: dict = None,
              start_datetime: datetime = None, end_datetime: datetime = None,
              item_ids: list = None, where: str = None, orderby: str = None,
              limit: int = None):
        """
        Generator that performs a query on the catalog with the given filters, requesting
        additional pages as necessary.
        """
        page = 0
        feature_count = 0
        while True:
            # Using this logic we make one more request than we have to.  But this way
            # we don't have to know what the service's page size limit is.
            page += 1
            Catalog.logger.info(f'Query page {page}')
            feature_coll = self.search(collections=collections, bbox=bbox, intersects=intersects,
                                       start_datetime=start_datetime, end_datetime=end_datetime,
                                       item_ids=item_ids, where=where, orderby=orderby,
                                       limit=limit, page=page)
            for feature in feature_coll.features:
                yield feature
            num_features = len(feature_coll.features)
            feature_count += num_features
            if not num_features:
                Catalog.logger.info(f'Total features returned: {feature_count}')
                return

    def collection_audit(
            self,
            collection_id: str,
            insert_datetime: Tuple[Optional[datetime], Optional[datetime]] = None,
            update_datetime: Tuple[Optional[datetime], Optional[datetime]] = None,
            desc: bool = False,
            page: int = None,
            limit: int = None):
        """

        """

        def parse_datetime_range(datetime_range: Tuple[Optional[datetime], Optional[datetime]]) -> str:
            try:
                (start_datetime, end_datetime) = datetime_range
            except Exception:
                raise Exception('start_datetime or end_datetime must be 2-element tuple')
            if not (start_datetime is None or isinstance(start_datetime, datetime)):
                raise Exception("Start datetime must be of type datetime or None")
            if not (end_datetime is None or isinstance(end_datetime, datetime)):
                raise Exception("End datetime must be of type datetime or None")
            if start_datetime and end_datetime:
                return '{}/{}'.format(
                    Catalog.format_datetime_iso8601(start_datetime),
                    Catalog.format_datetime_iso8601(end_datetime))
            elif start_datetime:
                return '{}/..'.format(Catalog.format_datetime_iso8601(start_datetime))
            else:
                return '../{}'.format(Catalog.format_datetime_iso8601(end_datetime))

        parameters = {}
        if not ((insert_datetime is None) ^ (update_datetime is None)):
            raise Exception('Exactly one of the insert_datetime or update_datetime parameters must be specified')
        if insert_datetime:
            parameters['audit_insert_date'] = parse_datetime_range(insert_datetime)
        else:
            parameters['audit_update_date'] = parse_datetime_range(update_datetime)

        if desc is not None:
            parameters['sortby'] = 'DESC'
        if limit is not None:
            parameters['limit'] = limit
            if page is not None:
                parameters['page'] = page
        elif page is not None:
            raise Exception('page may not be specified without limit')

        for (key, value) in parameters.items():
            Catalog.logger.info(f'Audit {key}: {value}')
        return self._call_api(self._coll_api.get_audit_search_with_http_info, collection_id, **parameters)

    def get_url(self, url: str) -> bytes:
        """
        Perform an HTTP GET on a catalog URL.
        :param url: Any catalog URL that supports GET.
        :return: Response body as bytes
        """
        logging.info(f'GET {url}')
        return self._request_url(requests.get, url)

    def get_url_json(self, url: str):
        """
        Perform an HTTP GET on a URL from an item's assets, and parse
        the response as JSON.
        :param url: URL from an item's asset's href property
        :return: Parsed JSON, generally returning a dict
        """
        logging.info(f'GET {url}')
        response = self._request_url(requests.get, url)
        try:
            return json.loads(str(response, encoding='utf-8'))
        except Exception as exp:
            raise CatalogError(f'Response from URL is not JSON: {url}') from exp

    def _call_api(self, function, *args, **kwargs):
        """
        Call a Swagger client method and process its response.

        :param function: Swagger client method to call
        :param args: Arbitrary arguments to pass to function
        :param kwargs: Arbitrary keyword arguments to pass to function
        :raises CatalogError: if error returned by web service
        :return: Service response parsed as a model object
        """

        try:
            with Catalog.timer():
                (body, status_code, headers) = function(*args, **kwargs)
            Catalog.logger.info(f'HTTP Status: {status_code}')

            request_id = headers.get('X-Maxar-RequestId')
            if request_id:
                Catalog.logger.info(f'Request ID: {request_id}')

            # Secret feature:  Stash response so user can examine it in case of error
            self.last_response = body
            return body
        except maxarcat_client.rest.ApiException as exp:
            # Upon errors the Catalog methods generally return JSON with a "message" property.
            # API Gateway as well sometimes returns JSON with a "message" property.
            # So try to raise our own exception with the message if possible.
            Catalog.logger.info(f'HTTP Status: {exp.status}')
            try:
                body = json.loads(exp.body)
                message = body['message']
                request_id = exp.headers.get('X-Maxar-RequestId')
            except Exception:
                # Fallback on generic error
                raise CatalogError(f'Service error:  HTTP status {exp.status} returned.', status=exp.status) from exp
            else:
                raise CatalogError(message, status=exp.status, request_id=request_id) from exp

    def _request_url(self, function, *args, **kwargs):
        """
        Process a call to a requests method
        :param function: Method in the requests package, e.g. requests.get
        :param args: Arbitrary arguments to pass to function
        :param kwargs: Arbitrar keyword arguments to pass to function
        :return: Response body
        """
        try:
            headers = {
                'Authorization': f'Bearer {self._token}'
            }
            with Catalog.timer():
                response = function(*args, **kwargs, headers=headers)
        except Exception as exp:
            Catalog.logger.error(exp)
            raise

        Catalog.logger.info(f'HTTP Status: {response.status_code}')

        request_id = response.headers.get('X-Maxar-RequestId')
        if request_id:
            Catalog.logger.info(f'Request ID: {request_id}')

        if 200 <= response.status_code < 300:
            return response.content

        # For errors we expect the response to have a JSON properties "message" and "request_id"
        try:
            body = json.loads(response.text)
            message = body['message']
        except Exception:
            # Fallback for any unrecognized error
            raise CatalogError(
                f'Service error:  HTTP status {response.status_code} returned.', response, request_id)
        else:
            raise CatalogError(message, response, request_id)

    @staticmethod
    def format_datetime_iso8601(dt: datetime):
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
