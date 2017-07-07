#!/usr/bin/env python

import pexpect
import time
from getpass import getpass

ip_addr = raw_input("Enter IP address: ")
username = 'pyclass'
password = getpass()
port = 22

ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
ssh_conn.timeout = 3

ssh_conn.expect('ssword:')
ssh_conn.sendline(password)
ssh_conn.expect('#')

ssh_conn.sendline('terminal length 0')
ssh_conn.expect('#')

ssh_conn.sendline('show ip int brief')
ssh_conn.expect('#')

print '\n>>>>'
print ssh_conn.before
print '>>>>\n'

