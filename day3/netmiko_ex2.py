#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler

def main():
    """Exercises using Netmiko"""
    passwd = getpass("Enter password: ")

    jnpr1 = {
        'device_type': 'juniper_junos',
        'host':   'juniper1.twb-tech.com',
        'username': 'pyclass',
        'password': passwd,
    }
    jnpr2 = {
        'device_type': 'juniper_junos',
        'host':   'juniper2.twb-tech.com',
        'username': 'pyclass',
        'password': passwd,
    }

    cfg_commands = [
        'set system syslog file messages any error',
    ]

    for a_device in [jnpr1, jnpr2]:
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
