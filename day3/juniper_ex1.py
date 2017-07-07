#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

from my_devices import juniper1, juniper2, juniper3, juniper4

print()
for vmx in [juniper1, juniper2, juniper3, juniper4]:
    a_device = Device(**vmx)
    a_device.open()
    print()
    print("-" * 60)
    pprint(a_device.facts)
    print("-" * 60)
    print()

print()
