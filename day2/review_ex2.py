#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint

with open("show_arp.txt") as f:
    output = f.readlines()

ip_dict = {}
for line in output:
    line = line.strip()
    if 'Protocol' in line:
        continue
    _, ip_address, age, mac_address, _, intf = line.split()
    ip_dict[ip_address] = mac_address

mac_dict = {}
for k, v in ip_dict.items():
    mac_dict[v] = k

print()
print("IP Address to Mac mapping")
print('-' * 50)
pprint(ip_dict)
print("\n")
print()
print("Mac Address to IP mapping")
print('-' * 50)
pprint(mac_dict)
print()
