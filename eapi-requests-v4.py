#!/usr/bin/env python3
# -*- coding=utf-8 -*-


from pyeapi import connect_to


if __name__ == "__main__":
    # devices = ['192.168.50.205', '192.168.50.207']
    device = connect_to('192.168.50.205')
    rsp = device.enable('show vlan brief')

    print(rsp)



