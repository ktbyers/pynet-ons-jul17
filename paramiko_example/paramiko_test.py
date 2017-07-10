#/usr/bin/env python
from __future__ import print_function, unicode_literals
from getpass import getpass
import time
import paramiko

ip_addr = '184.105.247.70'
username = 'pyclass'
password = getpass()

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip_addr, username=username, password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
time.sleep(1)
remote_conn.send("\n")
time.sleep(1)

output = remote_conn.recv(10000)
remote_conn.send("show ip int brief\n")
time.sleep(1)
output = remote_conn.recv(10000)
print(output)
