# -*- coding: utf-8 -*-

"""Main module."""

import requests

class Client:
    def __init__(self, api_key):
        self.base_url = 'https://app.whetstoneeducation.com'
        self.session = requests.Session()
        self.session.headers['x-key'] = api_key

    def auth(self):
        api_auth_url = f'{self.base_url}/auth/api'
        api_auth_payload = {
            'apikey': self.session.headers['x-key'],
        }

        api_auth_response = self.session.post(url=api_auth_url, data=api_auth_payload)
        
        api_auth_response_dict = api_auth_response.json()
        self.session.headers['x-access-token'] = api_auth_response_dict.get('token')
