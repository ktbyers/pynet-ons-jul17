#!/usr/bin/env python
from __future__ import print_function
from getpass import getpass
from pprint import pprint as pp
from napalm_base import get_network_driver

host = 'juniper1.twb-tech.com'
username = 'pyclass'
password = getpass()
optional_args = {}

driver = get_network_driver('junos')
device = driver(host, username, password, optional_args=optional_args)
device.open()

print()
print(">>>Load config change (replace)")
device.load_replace_candidate(filename='juniper1.conf')
print(device.compare_config())
prompt = raw_input("Continue (y/n): ")
if 'y' in prompt.lower():
    print("Commit change")
    device.commit_config()
else:
    print("Discard change")
    device.discard_config()
print()
