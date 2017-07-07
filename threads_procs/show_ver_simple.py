#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device = {
    'device_type': 'juniper_junos',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': getpass(),
    'port': 22,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command_expect("show version")

print()
print('#' * 50)
print(output)
print('#' * 50)
print()
