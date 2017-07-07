#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals

class NetDevice(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        self.serial_number = ''
        self.vendor = ''
        self.model = ''
        self.os_version = ''
        self.uptime = ''

    def print_ip(self):
        print("Device IP address is: {}".format(self.ip_addr))

    def print_credentials(self):
        print("Device username: {}".format(self.username))
        print("Device password: {}".format(self.password))

    def set_vendor(self, vendor):
        self.vendor = vendor
        print("Setting vendor to: {}".format(self.vendor))


if __name__ == "__main__":

    print()
    # Validation code
    my_obj1 = NetDevice(ip_addr='1.1.1.1', username='admin', password='pwd')
    my_obj1.print_ip()
    my_obj1.print_credentials()
    my_obj1.set_vendor("Cisco")
    print()
