#!/usr/bin/env python
from getpass import getpass
from pprint import pprint as pp
from napalm_base import get_network_driver

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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
print ">>>Load config change (merge) - no commit"
device.load_merge_candidate(filename='nxos_merge.conf')
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
device.load_merge_candidate(filename='nxos_merge.conf')
print device.compare_config()
device.commit_config()
print
raw_input("Hit any key to continue: ")
