#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
import sys
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()

if __name__ == "__main__":
    auth = HTTPBasicAuth('admin', 'admin')

    url = 'http://192.168.50.204/command-api'
    payload =  {
            "jsonrpc": "2.0",
            "method": "runCmds",
            "params": {
                "format": "json",
                "timestamps": False,
                "autoComplete": False,
                "expandAliases": False,
                "cmds": [
                    "show vlan brief"
                ],
                "version": 1
            },
            "id": "EapiExplorer-1"
        }

    response = requests.post(url, data=json.dumps(payload), auth=auth)
    # print('STATUS CODE: ' + str(response.status_code))

    # print('RESPONSE:')
    # results = json.loads(response.text)
    # print(json.dumps(results, indent=4))
    rsp = json.loads(response.text)
    vlans = rsp['result'][0]['vlans']



    print('{:12}{:10}{:>15}'.format('VLAN ID', 'NAME', 'STATUS'))
    for vlan_id, config in vlans.items():
        print('{:<12}{:<10}{:>15}'.format(vlan_id, config['name'], config['status']))

