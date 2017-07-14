"""
pynet-sw1  (Arista EOS) 184.105.247.72
pynet-sw2  (Arista EOS) 184.105.247.73
pynet-sw3  (Arista EOS) 184.105.247.74
pynet-sw4  (Arista EOS) 184.105.247.75
"""
from getpass import getpass

std_pwd = getpass("Enter standard password: ")

pynet_sw1 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.72',
    'username': 'pyclass',
    'password': std_pwd,
    'global_delay_factor': 2,
}

pynet_sw2 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.73',
    'username': 'pyclass',
    'password': std_pwd,
    'global_delay_factor': 2,
}

pynet_sw3 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.74',
    'username': 'pyclass',
    'password': std_pwd,
    'global_delay_factor': 2,
}

pynet_sw4 = {
    'device_type': 'arista_eos',
    'ip': '184.105.247.75',
    'username': 'pyclass',
    'password': std_pwd,
    'global_delay_factor': 2,
}

device_list = [
        pynet_sw1,
        pynet_sw2,
        pynet_sw3,
        pynet_sw4,
]
