#
# conftest.py
#
# Pytest fixtures.
#


import os

import pytest

from maxarcat import Catalog


@pytest.fixture(scope='session')
def maxarcat_token() -> str:
    try:
        return os.environ['MAXARCAT_TOKEN']
    except Exception:
        pytest.exit('Must set environment variable MAXARCAT_TOKEN to run tests', returncode=1)


@pytest.fixture(scope='session')
def maxar_catalog_url() -> str:
    return os.environ.get('MAXAR_CATALOG_URL', 'https://api.content.maxar.com/catalog')


@pytest.fixture(scope='session')
def catalog(maxarcat_token, maxar_catalog_url) -> Catalog:
    return Catalog(token=maxarcat_token, url=maxar_catalog_url)
