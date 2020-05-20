#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth('ntc', 'ntc123')
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }
    url = 'http://192.168.50.208/restconf/api/config/native/interface/GigabitEthernet/1/ip/address'
    response = requests.get(url, headers=headers, auth=auth).json

    # response = json.loads(response.text)
    # response = response.text
    print(response)
    # print(json.dumps(response, indent=4))