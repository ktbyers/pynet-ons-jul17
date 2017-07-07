#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from lxml import etree
import xmltodict

from my_devices import juniper2 as juniper_mx


if __name__ == "__main__":
    a_device = Device(**juniper_mx)
    a_device.open()

    xml_out = a_device.rpc.get_lldp_neighbors_information()
    my_dict = xmltodict.parse(etree.tostring(xml_out, encoding='unicode'))

    lldp_list = my_dict['lldp-neighbors-information']['lldp-neighbor-information']
    for lldp in lldp_list:
        local_port = lldp['lldp-local-port-id']
        remote_port = lldp['lldp-remote-port-id']
        remote_system_name = lldp['lldp-remote-system-name']

        print()
        print("Local Port: {}".format(local_port))
        print("Remote Port: {}".format(remote_port))
        print("Remote System: {}".format(remote_system_name))
        print()
