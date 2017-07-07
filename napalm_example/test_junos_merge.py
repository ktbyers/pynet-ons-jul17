#!/usr/bin/env python
from getpass import getpass
from pprint import pprint as pp
from napalm_base import get_network_driver

ip_addr = '184.105.247.76'
username = 'pyclass'
password = getpass()
optional_args = {}

driver = get_network_driver('junos')
device = driver(ip_addr, username, password, optional_args=optional_args)

print
print(">>>Test device open")
device.open()

print 
print ">>>Load config change (merge) - no commit"
device.load_merge_candidate(filename='junos-merge.conf')
print device.compare_config()
raw_input("Hit enter key to continue: ")

print 
print ">>>Discard config change (merge)"
device.discard_config()
print device.compare_config()
raw_input("Hit enter key to continue: ")

print 
print ">>>Load config change (merge) - commit"
device.load_merge_candidate(filename='junos-merge.conf')
print device.compare_config()
device.commit_config()
raw_input("Hit enter key to continue: ")

print 
print ">>>Rollback"
device.rollback()
