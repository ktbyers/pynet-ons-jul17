#!/usr/bin/env python
from getpass import getpass
from pprint import pprint as pp

from napalm_base import get_network_driver

host = '184.105.247.76'
username = 'pyclass'
password = getpass()
optional_args = {}

driver = get_network_driver('junos')
device = driver(host, username, password, optional_args=optional_args)

print
print(">>>Test device open")
device.open()

print
print(">>>Test get facts")
device_facts = device.get_facts()
pp(device_facts)
raw_input("Hit enter key to continue: ")

print
print(">>>Test get lldp neighbors")
#device_int = device.get_lldp_neighbors()
device_int = device.get_lldp_neighbors_detail()
pp(device_int)
raw_input("Hit enter key to continue: ")

print
print ">>>Test get environment"
env = device.get_environment()
pp(env)
raw_input("Hit enter key to continue: ")

print
print ">>>Test get bgp neighbors"
bgp_neigh = device.get_bgp_neighbors()
pp(bgp_neigh)
raw_input("Hit enter key to continue: ")
