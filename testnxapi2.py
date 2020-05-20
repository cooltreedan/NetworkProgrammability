#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
import requests
from pprint import pprint



if __name__ == "__main__":
    headers = {'Content-Type': 'application/json'}
    url = 'http://192.168.50.203/ins'

    switchuser = 'homelab'
    switchpassword = 'homelab123'

    payload = {
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show ip interface brief",
        "output_format": "json"
      }
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers, auth=(switchuser, switchpassword)).json()

    pprint(response)
