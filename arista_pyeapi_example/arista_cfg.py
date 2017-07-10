#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint
import pyeapi
import sys

###show_run = pynet_sw.running_config
###print show_run

def hit_key():
    try:
        raw_input("\n\nHit a key to continue: ")
    except NameError:
        input("\n\nHit a key to continue: ")

print("\n\nConfig VLAN 901:")
pynet_sw = pyeapi.connect_to("pynet-sw4")
return_val = pynet_sw.config(['vlan 901', 'name red'])
print(return_val)
hit_key()


print("\n\nVLAN API:")
vlan = pynet_sw.api('vlans')
vlan.create(902)
vlan.set_name(902, name='blue')
hit_key()

print("\n\nVLAN 902 Status:")
print(vlan.get(902))

#set_state
#set_trunk_groups

# Other APIs
#intf = pynet_sw.api('switchports')

print("\n\nSave Config")
pynet_sw.enable("write memory")
