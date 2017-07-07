#!/usr/bin/env python
import getpass
import snmp_helper

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
ip_addr1 = raw_input("pynet-rtr1 IP address: ")
community_string = getpass.getpass(prompt="Community string: ")
pynet_rtr1 = (ip_addr1, community_string, 161)

snmp_data = snmp_helper.snmp_get_oid(pynet_rtr1, oid=SYS_DESCR)
output = snmp_helper.snmp_extract(snmp_data)
print output
