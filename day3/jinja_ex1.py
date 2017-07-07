#!/usr/bin/env python
from __future__ import print_function
import jinja2

template_file = 'juniper_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

my_vars = {
    'neighbor1_ip' : '10.100.1.7',
    'neighbor1_as' : 22,
    'neighbor2_ip' : '10.100.99.1',
    'neighbor2_as' : 17,
    'neighbor3_ip' : '10.100.8.1',
    'neighbor3_as' : 88,
}

template = jinja2.Template(bgp_template)
print(template.render(my_vars))

