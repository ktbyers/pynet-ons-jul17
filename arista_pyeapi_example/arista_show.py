#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint
import pyeapi
import sys

def hit_key():
    try:
        raw_input("\n\nHit a key to continue: ")
    except NameError:
        input("\n\nHit a key to continue: ")

print("\n\nshow interfaces:")
pynet_sw = pyeapi.connect_to("pynet-sw4")
show_int = pynet_sw.enable("show interfaces")
pprint(show_int)
hit_key()

print("\n\nshow arp:")
output = pynet_sw.enable("show arp")
pprint(output)
hit_key()

print("\n\nshow route:")
output = pynet_sw.enable("show ip route")
pprint(output)
hit_key()

print("\n\nshow VLAN:")
output = pynet_sw.enable("show vlan")
output = output[0]['result']['vlans']
pprint(output)
hit_key()

print("\n\nVLAN API:")
vlan = pynet_sw.api('vlans')
pprint(vlan.getall())
hit_key()
print(vlan.get(1))
hit_key()
#print(vlan.get(101))
#hit_key()
