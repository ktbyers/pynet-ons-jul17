#!/usr/bin/env python
from getpass import getpass
from pprint import pprint as pp
from napalm_base import get_network_driver

host = '184.105.247.70'
username = 'pyclass'
password = getpass()
optional_args = {}

driver = get_network_driver('ios')
device = driver(host, username, password, optional_args=optional_args)

print
print "\n\n>>>Test device open"
device.open()


print
print ">>>Load config change (merge) - no commit"
device.load_merge_candidate(filename='ios_merge.conf')
print device.compare_config()
print
raw_input("Hit any key to continue: ")

print
print ">>>Discard config change (merge)"
device.discard_config()
print device.compare_config()
print
raw_input("Hit any key to continue: ")

print
print ">>>Load config change (merge) - commit"
device.load_merge_candidate(filename='ios_merge.conf')
print device.compare_config()
device.commit_config()
print
raw_input("Hit any key to continue: ")

print
print ">>>Load config change (replace) - commit"
device.load_replace_candidate(filename='pynet_rtr1.txt')
print device.compare_config()
#device.commit_config()
print
raw_input("Hit any key to continue: ")
#device.rollback()
