#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler

def main():
    """Exercises using Netmiko"""
    passwd = getpass("Enter password: ")

    srx1 = {
        'device_type': 'juniper_junos',
        'host':   'srx1.twb-tech.com',
        'username': 'pyclass',
        'password': passwd,
    }

    cfg_commands = [
        'set system syslog file messages any error',
    ]

    for a_device in [srx1]:
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        print("\nConfiguring Syslog + commit")
        print("#" * 80)
        output = net_connect.send_config_set(cfg_commands)
        output += net_connect.commit()
        print(output)
        print("#" * 80)
        print()


if __name__ == "__main__":
    main()
