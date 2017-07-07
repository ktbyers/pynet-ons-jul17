#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass

juniper_srx = {
    "host": "184.105.247.76",
    "user": "pyclass",
    "password": getpass(),
}

a_device = Device(**juniper_srx)
a_device.open()
eth_ports = EthPortTable(a_device)
eth_ports.get()
print eth_ports.keys()
