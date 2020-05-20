#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    auth = HTTPBasicAuth('homelab', 'homelab123')
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'http://192.168.50.203/ins'

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": 'show version',
            "output_format": "json"
        }
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)

    print(response)