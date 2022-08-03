#
# test_maxar_catalog.py
#
# Pytest test for maxarcat.
#

from datetime import datetime

import shapely.geometry


class TestCatalog:

    @staticmethod
    def test_healthcheck(catalog):
        response = catalog.get_healthcheck()
        print(response)

    @staticmethod
    def test_get_collections(catalog):
        collections = catalog.get_collections()
        print(f'Number of collections: {len(collections.collections)}')

    @staticmethod
    def test_get_collection(catalog):
        collection_ids = ['wv01', 'wv02', 'wv03-vnir', 'wv04']
        for collection_id in collection_ids:
            print(f'Reading collection {collection_id}')
            collection = catalog.get_collection(collection_id)
            print(collection)

    @staticmethod
    def test_get_collection_fails(catalog):
        assert catalog.get_collection('invalid') is None

    @staticmethod
    def test_get_item_fails(catalog):
        assert catalog.get_item('invalid') is None
        assert catalog.get_item('invalid', 'wv01') is None

    @staticmethod
    def test_search_bbox(catalog):
        feature_coll = catalog.search(bbox=[-105, 40, -104, 41])
        for feature in feature_coll.features:
            dt = feature.properties['datetime']
            print(f'Feature {feature.id} datetime={dt}')

    @staticmethod
    def test_search_no_filters(catalog):
        # It's allowed to search using no filters.  Given the search method's
        # default ordering of descending datetime this will return the newest
        # items in the catalog, up to the page size limit.
        features = catalog.search()
        print(f'Search with no filters returns {len(features.features)} items')

    @staticmethod
    def test_search_datetime_both(catalog):
        """
        Test searching on both start and end datetime.
        :param catalog: Pytest fixture
        """
        start = datetime(year=2020, month=1, day=1, hour=12)
        end = datetime(year=2020, month=1, day=2, hour=15)
        collection = 'wv02'
        feature_coll = catalog.search(collections=[collection], start_datetime=start, end_datetime=end)
        count = 0
        for feature in feature_coll.features:
            dt = TestCatalog.parse_datetime_iso8601(feature.properties['datetime'])
            assert start <= dt < end
            assert feature.collection == collection
            count += 1
        print(f'Verified {count} features in datetime range {start}/{end}')

    @staticmethod
    def test_search_datetime_start(catalog):
        """
        Test searching by only a start datetime.
        :param catalog: Pytest fixture
        """
        start = datetime(year=2020, month=1, day=1, hour=12)
        collection = 'wv03-vnir'
        # Order by datetime ascending so that if the test fails we'll see earliest images first
        feature_coll = catalog.search(collections=[collection], start_datetime=start, orderby='datetime')
        for feature in feature_coll.features:
            dt = TestCatalog.parse_datetime_iso8601(feature.properties['datetime'])
            assert dt >= start
            assert feature.collection == collection

    @staticmethod
    def test_search_datetime_end(catalog):
        """
        Test searching by only an end datetime.
        :param catalog: Pytest fixture
        """
        end = datetime(year=2020, month=1, day=1, hour=12)
        collection = 'wv03-vnir'
        feature_coll = catalog.search(collections=[collection], end_datetime=end)
        for feature in feature_coll.features:
            dt = TestCatalog.parse_datetime_iso8601(feature.properties['datetime'])
            assert dt < end
            assert feature.collection == collection

    @staticmethod
    def test_get_item(catalog):
        # Get an arbitrary set of 10 items to test with
        feature_coll = catalog.search(collections=['wv02'], bbox=[-105, 40, -104, 41], limit=10)

        # No request each feature one at a time, both by just its ID and with
        # its collection ID.
        for feature in feature_coll.features:
            feature2 = catalog.get_item(feature.id)
            assert feature == feature2
            feature3 = catalog.get_item(feature.id, feature.collection)
            assert feature == feature3
            # Try fetching item but from a different collection, must fail
            assert catalog.get_item(feature.id, 'wv01') is None

        # Now test fetching the same set of 10 features, this time all at
        # once with a list of IDs
        item_ids = [feature.id for feature in feature_coll.features]
        feature_coll = catalog.search(item_ids=item_ids)
        assert len(feature_coll.features) == len(item_ids)
        for feature in feature_coll.features:
            assert feature.id in item_ids

        # Now search again but specify complete=False.  None of these items is incomplete -- we
        # just want to test that the search method correctly parses its complete parameter.
        feature_coll = catalog.search(item_ids=item_ids, complete=False)
        assert len(feature_coll.features) == len(item_ids)
        for feature in feature_coll.features:
            assert feature.id in item_ids


    @staticmethod
    def test_search_intersects(catalog):
        """
        Test searching on a intersection polygon
        :param catalog: Pytest fixture
        """

        # Get an arbitrary set of 10 items to test with
        test_features = catalog.search(bbox=[-105, 40, -104, 41], limit=10)

        # Now search on each feature's polygon
        for feature in test_features.features:
            features = catalog.search(intersects=feature.geometry)

            # The feature itself must be among the returned features
            ids = {f.id for f in features.features}
            assert feature.id in ids

            # Each returned feature must intersect the requested polygon
            polygon = shapely.geometry.shape(feature.geometry)
            for f in features.features:
                assert polygon.intersects(shapely.geometry.shape(f.geometry))

    @staticmethod
    def test_search_where(catalog):
        # Get an arbitrary set of 10 items to test with
        where = 'eo:cloud_cover < 20'
        features = catalog.search(bbox=[-105, 40, -104, 41], where=where)
        for feature in features.features:
            assert feature.properties['eo:cloud_cover'] < 20

    @staticmethod
    def test_search_paging(catalog):
        # Get a set of features to test with
        features = catalog.search(collections=['wv01'])
        print(f'Paging through {len(features.features)} features')

        # In general when paging through a selection it's possible for the
        # set of selected items to change in between pages.
        # For this test we search on a fixed set of item ID's to try to
        # avoid this problem.
        ids = [feature.id for feature in features.features]
        page_size = 10
        page = 0
        received_ids = set()
        while True:
            page += 1
            print(f'Requesting page {page} of size {page_size}')
            batch = catalog.search(item_ids=ids, page=page, limit=page_size)
            batch_ids = {feature.id for feature in batch.features}
            if not batch_ids:
                break
            assert batch_ids <= set(ids)
            assert batch_ids.isdisjoint(received_ids)
            received_ids |= batch_ids
        assert received_ids == set(ids)

    @staticmethod
    def test_query(catalog):
        """
        Test the query method on a search that we know requires paging.
        :param catalog: Pytest fixture
        """

        # At the time of writing the service has a hard limit of 100 items
        # per page.  Assume that's still the case and perform a query
        # that should return thousands of items.  Stop after we've read
        # what should be a few pages.
        features = catalog.query(bbox=[-100, 40, -105, 45])
        count = 0
        for _ in features:
            count += 1
            if count >= 500:
                break

    @staticmethod
    def test_assets(catalog):
        # Get a few of the most recent WV02 images and verify that we can
        # read their browse, cloud-cover, and sample-point-set assets.
        feature_coll = catalog.search(collections=['wv02'], limit=3)
        for feature in feature_coll.features:
            print(f'Fetching assets for {feature.id}')
            catalog.get_url(feature.assets['browse']['href'])
            catalog.get_url_json(feature.assets['cloud-cover']['href'])
            catalog.get_url_json(feature.assets['sample-point-set']['href'])

    @staticmethod
    def test_links(catalog):
        # Get a few of the most recent WV03 images and verify that they
        # have links.  We expect any Maxar image to have at least a "self"
        # and a "collection" link.
        collection_name = 'wv03-vnir'
        feature_coll = catalog.search(collections=[collection_name], limit=3)
        for feature in feature_coll.features:
            print(f'Fetching links for {feature.id}')

            # Fetch the collection link
            hrefs = [link['href'] for link in feature.links if link['rel'] == 'collection']
            assert hrefs, 'Item has no collection link'
            collection_url = hrefs[0]
            collection = catalog.get_url_json(collection_url)
            assert collection['id'] == collection_name

            # Fetch the self link
            hrefs = [link['href'] for link in feature.links if link['rel'] == 'self']
            assert hrefs, 'Item has no self link'
            item_url = hrefs[0]
            item = catalog.get_url_json(item_url)
            assert item['id'] == feature.id

    @staticmethod
    def test_parse_datetime_iso8601():
        assert TestCatalog.parse_datetime_iso8601('2020-01-02T03:04:05Z') == datetime(2020, 1, 2, 3, 4, 5)
        assert TestCatalog.parse_datetime_iso8601('2020-01-02T03:04:05.5Z') == datetime(2020, 1, 2, 3, 4, 5, 500000)
        assert TestCatalog.parse_datetime_iso8601('2020-01-02T03:04:05.123Z') == datetime(2020, 1, 2, 3, 4, 5, 123000)

    @staticmethod
    def parse_datetime_iso8601(value):
        # Try to parse with and without fractional seconds
        try:
            return datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        except Exception:
            pass
        try:
            return datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        except Exception:
            raise Exception(f'Could not parse datetime: {value}')
