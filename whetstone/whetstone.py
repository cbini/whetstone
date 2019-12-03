# -*- coding: utf-8 -*-

"""Main module."""

import requests


class Client:
    """Base client for interacting with the Whetstone API.
    """
    def __init__(self):
        self.base_url = 'https://app.whetstoneeducation.com'
        self.session = requests.Session()

    def authorize(self, api_key):
        """Obtains an access token to for use with API calls.

        :param api_key: Your API key
        :type api_key: str
        """
        url = f'{self.base_url}/auth/api'
        payload = {
            'apikey': api_key,
        }

        response = self.session.post(url=url, data=payload)
        response_data = response.json()

        self.session.headers['x-key'] = api_key
        self.session.headers['x-access-token'] = response_data.get('token')
