#!/usr/bin/env python
"""
SNMP query all of the interfaces on the pynet-rtr1 using SNMPv3.
Get the interface description and the in_octets/out_octets
"""
from __future__ import print_function, unicode_literals
from getpass import getpass
from snmp_helper import snmp_get_oid_v3, snmp_extract

IFDESCR = '1.3.6.1.2.1.2.2.1.2.'
IFINOCTETS = '1.3.6.1.2.1.2.2.1.10.'
IFOUTOCTETS = '1.3.6.1.2.1.2.2.1.16.'


def main():
    """
    SNMP query all of the interfaces on the pynet-rtr1 using SNMPv3.
    Get the interface description and the in_octets/out_octets
    """
    my_key = getpass(prompt="Auth + Encryption Key: ")

    # SNMPv3 Connection Parameters
    ip_addr = '184.105.247.70'
    a_user = 'pysnmp'
    auth_key = my_key
    encrypt_key = my_key
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (ip_addr, 161)

    print()
    print("{:>15} {:>15} {:>15}".format("IfDescr", "IfInOctets", "IfOutOctets"))
    for if_index in range(1, 8):
        results = []
        for base_oid in (IFDESCR, IFINOCTETS, IFOUTOCTETS):
            the_oid = base_oid + str(if_index)
            snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=the_oid)
            results.append(snmp_extract(snmp_data))
        print("{:>15} {:>15} {:>15}".format(*results))
    print()

if __name__ == "__main__":
    main()
