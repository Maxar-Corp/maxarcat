#
# examples.py
#
# Demonstrate maxarcat Catalog's search and query methods.
#

import argparse
from datetime import datetime

from maxarcat import Catalog


class Examples:
    def __init__(self, token):
        self.catalog = Catalog(token=token)

    def search_example(self):
        """
        Call search method and page until all items returned.
        """
        limit = 1000
        page = 0
        while True:
            page += 1
            print(f'Querying page {page}')
            result = self.catalog.search(
                collections=['imagery'],
                start_datetime=datetime(2023, 8, 1),
                end_datetime=datetime(2023, 8, 2),
                page=page,
                limit=limit)
            print(f'Feature count: {len(result.features)}')
            # Stop page requests if there is no "next" link
            if result.links is None or not any([link['rel'] == 'next' for link in result.links]):
                break

    def query_example(self):
        """
        Call query method and let it perform paging
        """
        result = self.catalog.query(
            collections=['imagery'],
            start_datetime=datetime(2023, 8, 1),
            end_datetime=datetime(2023, 8, 2))
        # Use generator expression to force all pages to be read
        features = list((result))
        print(f'Feature count: {len(features)}')


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', required=True)
    args = parser.parse_args()
    token = args.token

    examples = Examples(token)
    print('Test search method')
    examples.search_example()
    print()
    print('Test query method')
    examples.query_example()


if __name__ == '__main__':
    run()
