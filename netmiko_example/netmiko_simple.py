#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    srx = {
        'device_type': 'juniper_junos',
        'ip':   '184.105.247.76',
        'username': 'pyclass',
        'password': password
    }

    net_connect = ConnectHandler(**srx)
    print(net_connect.find_prompt())
