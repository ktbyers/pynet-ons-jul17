#!/usr/bin/env python
from __future__ import print_function
from pprint import pprint

def read_file(filename):
    with open(filename) as f:
        return f.read()

def find_serial_number(show_ver):
    for line in show_ver.splitlines():
        if 'Processor board ID' in line:
            _, serial_number = line.split("Processor board ID")
            return serial_number
    return ''

def find_vendor(show_ver):
    for line in show_ver.splitlines():
        if 'Cisco IOS Software' in line:
            return 'Cisco'
    return ''

def find_model(show_ver):
    for line in show_ver.splitlines():
        if 'bytes of memory' in line:
            model, _ = line.split('processor')
            return model.split()[1]
    return ''

def find_os_version(show_ver):
    '''Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)'''
    for line in show_ver.splitlines():
        if 'Cisco IOS Software' in line:
            os_version = line.split(',')[2]
            return os_version.split()[1]
    return ''

def find_uptime(show_ver):
    for line in show_ver.splitlines():
        if 'uptime is' in line:
            return line.split('uptime is ')[1]
    return ''


my_file = "show_version.txt"

my_device = {}

show_ver = read_file(my_file)
my_device['serial_number'] = find_serial_number(show_ver)
my_device['vendor'] = find_vendor(show_ver)
my_device['model'] = find_model(show_ver)
my_device['os_version'] = find_os_version(show_ver)
my_device['uptime'] = find_uptime(show_ver)

print()
pprint(my_device)
print()
