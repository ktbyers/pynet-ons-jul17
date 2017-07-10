#!/usr/bin/env python
"""jsonrpclib doesn't support PY3 currently (2017-07-10)."""
from __future__ import print_function, unicode_literals
import ssl
import jsonrpclib
from pprint import pprint
from getpass import getpass

ssl._create_default_https_context = ssl._create_unverified_context

ip = '184.105.247.72'
port = '443'
username = 'pyclass'
password = getpass()

url = 'https://{}:{}@{}:{}/command-api'.format(username, password, ip, port)

print(url)
eapi_connect = jsonrpclib.Server(url)
response = eapi_connect.runCmds(1, ['show version'])
pprint(response)

