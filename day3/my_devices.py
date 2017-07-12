"""
pynet-rtr1 (Cisco IOS)  184.105.247.70
pynet-rtr2 (Cisco IOS)  184.105.247.71
pynet-sw1  (Arista EOS) 184.105.247.72
pynet-sw2  (Arista EOS) 184.105.247.73
pynet-sw3  (Arista EOS) 184.105.247.74
pynet-sw4  (Arista EOS) 184.105.247.75
juniper-srx             184.105.247.76
"""
from getpass import getpass
password = getpass("Enter standard password: ")

cisco_rtr1 = dict(
    hostname='184.105.247.70',
    device_type='ios',
    username='pyclass',
    password=password,
    optional_args = {}
)

cisco_rtr2 = dict(
    hostname='184.105.247.71',
    device_type='ios',
    username='pyclass',
    password=password,
    optional_args = {}
)

arista_sw1 = dict(
    hostname='184.105.247.72',
    device_type='eos',
    username='pyclass',
    password=password,
    optional_args = {}
)

arista_sw2 = dict(
    hostname='184.105.247.73',
    device_type='eos',
    username='pyclass',
    password=password,
    optional_args = {}
)

juniper_srx = dict(
    hostname='184.105.247.76',
    device_type='junos',
    username='pyclass',
    password=password,
    optional_args = {}
)

juniper1 = dict(
    hostname='juniper1.twb-tech.com',
    device_type='junos',
    username='pyclass',
    password=password,
    optional_args = {}
)

juniper2 = dict(
    hostname='juniper2.twb-tech.com',
    device_type='junos',
    username='pyclass',
    password=password,
    optional_args = {}
)

device_list = [
        cisco_rtr1,
        cisco_rtr2,
        arista_sw1,
        arista_sw2,
        juniper_srx,
]

