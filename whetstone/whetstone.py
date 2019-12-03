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
        api_auth_url = f'{self.base_url}/auth/api'
        api_auth_payload = {
            'apikey': api_key,
        }

        api_auth_response = self.session.post(url=api_auth_url, data=api_auth_payload)        
        api_auth_response_dict = api_auth_response.json()
        
        self.session.headers['x-key'] = api_key
        self.session.headers['x-access-token'] = api_auth_response_dict.get('token')
