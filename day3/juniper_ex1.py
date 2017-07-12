#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

juniper_srx = {
    "host": "srx1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}

print()
for device in [juniper_srx]:
    a_device = Device(**device)
    a_device.open()
    print()
    print("-" * 60)
    pprint(a_device.facts)
    print("-" * 60)
    print()

print()
