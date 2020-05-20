#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader

device = ConnectHandler(host = '192.168.50.204', username = 'admin', password = 'admin', device_type = 'arista_eos')

interface_dict = {"name": "Ethernet6", "description": "Server Port", "vlan": 10, "uplink": False}

ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("config.j2")
commands = template.render(interface=interface_dict)

with open ('veos.conf', 'w') as config_file:
    config_file.writelines(commands)
    device.enable()
    output = device.send_config_from_file('veos.conf')
    output = device.send_config_from_file(config_file='veos.conf')

verification = device.send_command('show run interface Ethernet6')

print(verification)