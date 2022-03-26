# -*- coding:utf-8 -*-

import requests
import textwrap

class Fact:
    def __init__(self):
        pass

    def update(self, api_id):

        api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'
        response = requests.get(api_url, headers={'X-Api-Key': api_id})

        if response.status_code == requests.codes.ok:
            fact = response.text
        else:
            # set as fact to show on display
            fact = "Error:" + " " + response.status_code + " - " + response.text

        return fact
