#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    auth = HTTPBasicAuth('admin', 'cisco123')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "kind": "object#GigabitInterface",
        "interfaceDesc": "Configured by Python"
    }

    url = "https://192.168.50.200/api/interfaces/physical/GigabitEthernet0_API_SLASH_0"
    # response = requests.get(url, auth=auth, headers=headers, verify=False)
    response = requests.patch(url, data=json.dumps(payload), auth=auth, headers=headers, verify=False)