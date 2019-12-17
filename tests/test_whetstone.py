#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `whetstone` package."""

import pytest

from whetstone import whetstone

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_client_instantiation():
    import requests

    # instantiating a Client should return an object with the correct base_url
    # and a requests Session
    client = whetstone.Client()
    
    assert client.base_url == 'https://app.whetstoneeducation.com'
    assert isinstance(client.session, requests.sessions.Session)
