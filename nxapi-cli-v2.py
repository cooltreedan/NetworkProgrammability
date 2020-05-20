#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
import sys
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    auth = HTTPBasicAuth('homelab', 'homelab123')

    url = 'http://192.168.50.203/ins'

    command = sys.argv[1]

    if len(sys.argv) > 2:
        command_type = sys.argv[2]
    else:
        command_type = 'cli_show'

    payload = {
        "ins_api": {
            "version": "1.0",
            "type": command_type,
            "chunk": "0",
            "sid": "1",
            "input": command,
            "output_format": "json"
        }
    }

    response = requests.post(url, data=json.dumps(payload), auth=auth)


    print('STATUS CODE: '+ str(response.status_code))

    print('RESPONSE: ')
    results= json.loads(response.text)
    print(json.dumps(results, indent=4))