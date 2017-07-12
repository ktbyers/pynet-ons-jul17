#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

juniper_mx = {
    "host": "juniper1.twb-tech.com",
    "user": "pyclass",
    "password": getpass(),
}

a_device = Device(**juniper_mx)
a_device.open()
a_device.timeout = 90
cfg = Config(a_device)

print "\nConfiguring IP using {} notation (external file)"
cfg.load(path="configure_ip.conf", format="text", merge=False)

print "Current config differences: "
print cfg.diff()

print "Performing commit"
cfg.commit()
