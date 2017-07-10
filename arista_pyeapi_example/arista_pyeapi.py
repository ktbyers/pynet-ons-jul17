#!/usr/bin/env python
from pprint import pprint
import pyeapi

pynet_sw = pyeapi.connect_to("pynet-sw4")
show_version = pynet_sw.enable("show version")
pprint(show_version)

