#!/usr/bin/env python
from __future__ import print_function

net_device = {
    'ip_addr': '172.30.220.1',
    'username': 'admin',
    'password': 'some_pass',
    'vendor': 'cisco',
    'model': '3945',
}

print()
for k, v in net_device.items():
    print(k, v)

net_device['password'] = 'new_value'
net_device['secret'] = 'some_secret'

device_type = net_device.get('device_type', 'cisco_ios')
print("\nDefault device type: {}\n".format(device_type))
