#!/usr/bin/env python
"""Idempotent configuration of VLAN IDs and names using Netmiko."""
import re
from netmiko import ConnectHandler
from my_devices import device_list

def check_vlan_exists(output):
    """
    Check whether VLAN id exists in the VLAN database.

    801   blue                             active

    % VLAN 801 not found in current VLAN database
    """
    pattern = r"%.*not found in current VLAN database"
    return not bool(re.search(pattern, output))

def check_vlan_name(output, vlan_name):
    """
    Check VLAN name
    801   blue                             active
    """
    return vlan_name in output

def add_vlan(net_connect, vlan_id, vlan_name=''):
    """Use Netmiko to add VLAN name and ID."""
    cmd1 = "vlan " + str(vlan_id)
    cmds = [cmd1,]
    if vlan_name:
        cmd2 = "name " + vlan_name
        cmds.append(cmd2)
    return net_connect.send_config_set(cmds)

def main():
    """Idempotent configuration of VLAN IDs and names using Netmiko."""
    print
    new_vlans = [
        ('801', 'blue'),
        ('802', 'red'),
        ('803', 'orange'),
    ]

    for a_device in device_list:
        net_conn = ConnectHandler(**a_device)
        device_name = net_conn.base_prompt
        print
        print '#' * 30
        print device_name
        print '#' * 30
        print

        for vlan_id, vlan_name in new_vlans:
            cmd = "show vlan id {}".format(vlan_id)
            print "Checking vlan_id: {}, vlan_name: {}".format(vlan_id, vlan_name)
            print '-' * 80
            output = net_conn.send_command(cmd)
            vlan_exists = check_vlan_exists(output)
            vlan_name_correct = check_vlan_name(output, vlan_name)
            if not vlan_exists or not vlan_name_correct:
                print "Adding vlan/updating vlan name...",
                print output
                output = add_vlan(net_conn, vlan_id, vlan_name)
                print "Done"
            else:
                print "VLAN exists and has correct name"
            print '-' * 80
            print
    print

if __name__ == "__main__":
    main()
