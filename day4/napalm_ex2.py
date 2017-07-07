#!/usr/bin/env python
from pprint import pprint as pp

from napalm_base import get_network_driver
from my_devices import juniper1, juniper2, cisco_rtr1

def main():
    for a_device in (juniper1, juniper2, cisco_rtr1):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        print
        print ">>>Device open"
        device.open()

        print "-" * 50
        device_facts = device.get_lldp_neighbors()
        pp(device_facts)
    print

if __name__ == "__main__":
    main()
