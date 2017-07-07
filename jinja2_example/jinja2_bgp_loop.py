#!/usr/bin/env python
from __future__ import print_function
import jinja2

template_file = 'bgp_loop.j2'
with open(template_file) as f:
    bgp_template = f.read()

my_vars = {
    "my_list": [
            ('10.100.1.7', 22),
            ('10.100.1.8', 23),
            ('10.100.1.9', 24),
    ]
}

template = jinja2.Template(bgp_template)
print(template.render(my_vars))

