from jnpr.junos import Device
from test_table.test_view import XArpTable

from lxml import etree
import xmltodict
import xml.etree.ElementTree as ET
from getpass import getpass
import time

juniper_mx = { 
    "host": "juniper1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}   

a_device = Device(**juniper_mx)
a_device.open()

test1 = XArpTable(a_device)
test1.get()

