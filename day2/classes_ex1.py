#!/usr/bin/env python
from __future__ import print_function

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


my_obj1 = NetDevice(ip_addr='1.1.1.1', username='admin', password='pwd')
my_obj2 = NetDevice(ip_addr='1.1.1.2', username='admin', password='pwd')
my_obj3 = NetDevice(ip_addr='1.1.1.3', username='admin', password='pwd')
my_obj4 = NetDevice(ip_addr='1.1.1.4', username='admin', password='pwd')
