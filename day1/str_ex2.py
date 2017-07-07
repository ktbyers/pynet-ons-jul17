#!/usr/bin/env python
from __future__ import print_function

try:
    # PY2
    ip_addr = raw_input("Please enter IP address: ")
except NameError:
    # PY3
    ip_addr = input("Please enter IP address: ")
    
ip_addr = ip_addr.split(".")

print()
print("{:<12} {:<12} {:<12} {:<12}".format(*ip_addr))
print()
