#!/usr/bin/env python
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

juniper_mx = { 
        "host": "juniper1.twb-tech.com",
        "user": "pyclass",
        "password": getpass(),
    }   

a_device = Device(**juniper_mx)
a_device.open()
pprint(a_device.facts)

