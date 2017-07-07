#!/usr/bin/env python
"""
http://www.juniper.net/documentation/en_US/junos-pyez/topics/task/program/junos-pyez-rpcs-executing.html
"""

from jnpr.junos import Device
from lxml import etree
import xmltodict
import xml.etree.ElementTree as ET
from getpass import getpass
from pprint import pprint
import time

juniper_mx = { 
    "host": "juniper1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}   

a_device = Device(**juniper_mx)
a_device.open()

if True:
    show_version = a_device.rpc.get_software_information()
#    print(etree.tostring(show_version, encoding='unicode'))
    show_version_json = a_device.rpc.get_software_information({'format':'json'})
    pprint(show_version_json)

if False:
    arp = a_device.rpc.get_arp_table_information()
    print(etree.tostring(arp, encoding='unicode'))
    show_arp_json = a_device.rpc.get_arp_table_information({'format':'json'})
    pprint(show_arp_json)

if False:
    route = a_device.rpc.get_route_information()
    print(etree.tostring(route, encoding='unicode'))
    my_dict = xmltodict.parse(etree.tostring(route, encoding='unicode'))



'''
Structure using xmltodict
>>> my_dict['route-information']['route-table']['rt'][0]['rt-destination']
u'0.0.0.0/0'
>>> my_dict['route-information']['route-table']['rt'][1]['rt-destination']
u'10.0.0.0/24'
>>> my_dict['route-information']['route-table']['rt'][2]['rt-destination']
u'10.0.0.31/32'
'''

'''
>>> route.tag
'route-information'
>>> route.attrib
{}

>>> for child in route:
...   print child.tag, child.attrib
... 
<cyfunction Comment at 0x7f8ee27974d0> <lxml.etree._ImmutableMapping object at 0x7f8ee2ed0610>
route-table {}
'''

time.sleep(5)
a_device.close()

