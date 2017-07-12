#!/usr/bin/env python
from pprint import pprint as pp

from napalm_base import get_network_driver
from my_devices import cisco_rtr1, juniper1

merge_files = {
    'cisco': 'cisco_merge.txt',
    'juniper': 'juniper_merge.txt',
}

def main():
    for a_device in (cisco_rtr1, juniper1):
        device_type = a_device.pop('device_type')
        driver = get_network_driver(device_type)
        device = driver(**a_device)

        if device_type == 'ios':
            filename = merge_files['cisco']
        elif device_type == 'junos':
            filename = merge_files['juniper']
        else:
            raise ValueError("Invalid device_type specified")

        print
        print ">>>Device open"
        device.open()

        print
        print ">>>Load config change (merge) - no commit"
        device.load_merge_candidate(filename=filename)
        print device.compare_config()

        print
        print ">>>Discard config change (merge)"
        device.discard_config()
        print device.compare_config()

        print
        print ">>>Load config change (merge) - commit"
        device.load_merge_candidate(filename=filename)
        print device.compare_config()
        device.commit_config()

    print

if __name__ == "__main__":
    main()
