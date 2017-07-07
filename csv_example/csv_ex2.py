#!/usr/bin/env python
"""
Expand on exercise1 except establish a Netmiko SSH connection using the CSV file
information.
"""
from __future__ import print_function
from __future__ import unicode_literals
import csv
from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException

PASSWORD = getpass()

def establish_netmiko_conn(device_name, netmiko_dict):
    """Establish Netmiko SSH connection; print device prompt."""
    try:
        print("\n")
        print('-' * 40)
        print("Establish SSH Conn: {}".format(device_name))
        netmiko_dict['password'] = PASSWORD
        net_conn = ConnectHandler(**netmiko_dict)
        print(net_conn.find_prompt())
        print('-' * 40)
        print("\n")
    except NetMikoAuthenticationException:
        print("SSH login failed")

def main():
    """
    Expand on exercise1 except establish a Netmiko SSH connection using the CSV file
    information.
    """
    file_name = "test_net_devices.csv"
    with open(file_name) as f:
        read_csv = csv.DictReader(f)
        for entry in read_csv:
            device_name = entry.pop('device_name')
            establish_netmiko_conn(device_name, entry)

if __name__ == "__main__":
    main()
