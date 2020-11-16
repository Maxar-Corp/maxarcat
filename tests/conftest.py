#
# conftest.py
#
# Pytest fixtures.
#


import os

import pytest

from maxarcat import Catalog



@pytest.fixture(scope='session')
def gbdx_token():
    try:
        return os.environ['GBDX_TOKEN']
    except Exception:
        pytest.exit('Must set environment variable GBDX_TOKEN to run tests', returncode=1)


@pytest.fixture(scope='session')
def maxar_catalog_url():
    return os.environ.get('MAXAR_CATALOG_URL', 'https://beta-api.content.maxar.com/catalog')


@pytest.fixture(scope='session')
def catalog(gbdx_token, maxar_catalog_url):
    return Catalog(token=gbdx_token, url=maxar_catalog_url)
