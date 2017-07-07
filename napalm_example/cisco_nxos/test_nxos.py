#!/usr/bin/env python
from getpass import getpass
from pprint import pprint as pp
from napalm_base import get_network_driver

host = 'nxos1.twb-tech.com'
username = 'pyclass'
password = getpass()
optional_args = {}
optional_args['nxos_protocol'] = 'https'
optional_args['port'] = 8443

driver = get_network_driver('nxos')
device = driver(host, username, password, optional_args=optional_args)

print
print "\n\n>>>Test device open"
device.open()

print
print "\n\n>>>Test get facts"
device_facts = device.get_facts()
pp(device_facts)
print
raw_input("Hit any key to continue: ")

print
print(">>>Test get lldp neighbors")
device_int = device.get_lldp_neighbors_detail()
pp(device_int)
print
raw_input("Hit any key to continue: ")

print
print ">>>Test get environment"
try:
    env = device.get_environment()
    pp(env)
except NotImplementedError:
    print "Not implemented."
print
raw_input("Hit any key to continue: ")

print
print ">>>Test get interfaces"
intf = device.get_interfaces()
pp(intf)
print
raw_input("Hit any key to continue: ")

