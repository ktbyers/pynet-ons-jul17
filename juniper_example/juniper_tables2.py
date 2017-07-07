#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.lldp import LLDPNeighborTable
from getpass import getpass
from pprint import pprint

juniper_srx = {
    "host": "juniper1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}

def juniper_print(k, v):
    print 
    print k
    print '-' * 20
    pprint(v)
    print '-' * 20

a_device = Device(**juniper_srx)
a_device.open()

eth_ports = EthPortTable(a_device)
eth_ports.get()
print '-' * 80
print "Ethernet Ports"
for k, v in eth_ports.items():
    juniper_print(k, v)
print '-' * 80
raw_input("Hit enter to continue: ")

arp = ArpTable(a_device)
arp.get()
print '-' * 80
print "ARP"
for k, v in arp.items():
    juniper_print(k, v)
print '-' * 80
raw_input("Hit enter to continue: ")

lldp = LLDPNeighborTable(a_device)
lldp.get()
print '-' * 80
print "LLDP Neighbors"
for k, v in lldp.items():
    juniper_print(k, v)
print '-' * 80
raw_input("Hit enter to continue: ")
print '-' * 80
