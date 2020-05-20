#!/usr/bin/env python3
# -*- coding=utf-8 -*-

# Import Jinja2 library and PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml

# Declare template environment
ENV = Environment(loader=FileSystemLoader('.'))

def get_interface_speed(interface_name):
    """
    get interface_speed return the default Mbps value for a given
    network interface by looking for certain keywords in the name
    """

    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

# Filters are added to ENV object after declaration. Note that we're
# actually passing in our "get_interface_speed" function and not running
# it -- the template engine will execute this function when we call
# template.render()

ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("templatestuff/template.j2")

# We load our YAML file and pass it to the template when rendering it.
with open("templatestuff/data.yml") as f:
    interfaces = yaml.load(f)
    print(template.render(interface_list=interfaces))