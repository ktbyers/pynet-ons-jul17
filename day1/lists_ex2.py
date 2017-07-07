#!/usr/bin/env python
from __future__ import print_function

try:
    # PY2
    ip_addr = raw_input("Please enter IP address: ")
except NameError:
    # PY3
    ip_addr = input("Please enter IP address: ")

my_ip_list = ip_addr.split(".")
my_ip_list[-1] = 0

ip_binary = []
ip_binary.append(bin(int(my_ip_list[0])))
ip_binary.append(bin(int(my_ip_list[1])))
ip_binary.append(bin(int(my_ip_list[2])))
ip_binary.append(bin(int(my_ip_list[3])))

print()
print("{:<12} {:<12} {:<12} {:<12}".format('octet1', 'octet2', 'octet3', 'octet4'))
print("{:<12} {:<12} {:<12} {:<12}".format(*my_ip_list))
print("{:<12} {:<12} {:<12} {:<12}".format(*ip_binary))
print()
