#!/usr/bin/env python
"""
In a file define a network device in YAML (compatible with Netmiko)
Read that file in and connect to the network device using Netmiko
Display show arp from that device
"""
from __future__ import print_function
from getpass import getpass
import yaml
from netmiko import ConnectHandler


def read_yml_file(filename):
    """Read YAML file"""
    with open(filename) as f:
        return yaml.load(f)

def main():
    """
    In a file define a network device in YAML (compatible with Netmiko)
    Read that file in and connect to the network device using Netmiko
    Display show arp from that device
    """
    filename = "my_device.yml"
    devices = read_yml_file(filename)
    password = getpass()
    for a_device in devices:
        device_name = a_device.pop('device_name')
        print("\n\nConnecting to: {}".format(device_name))
        a_device['password'] = password
        net_conn = ConnectHandler(**a_device)
        print(net_conn.send_command("show arp"))
        net_conn.disconnect()
    print()

if __name__ == "__main__":
    main()
