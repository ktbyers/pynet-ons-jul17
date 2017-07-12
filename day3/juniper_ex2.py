#!/usr/bin/env python
from __future__ import print_function

from jnpr.junos import Device
from lxml import etree
from getpass import getpass

juniper_srx = {
    "host": "srx1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}

if __name__ == "__main__":
    a_device = Device(**juniper_srx)
    a_device.open()

    # Convert <get-lldp-neighbors-information> to method call
    xml_out = a_device.rpc.get_lldp_neighbors_information()
    print()
    print(etree.tostring(xml_out, encoding='unicode'))
    print()
