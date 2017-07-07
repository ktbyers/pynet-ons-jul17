#!/usr/bin/env python
from __future__ import print_function

output_file = 'bgp_output.txt'

with open("show_ip_bgp.txt") as f:
    show_bgp = f.read()

header_lines, bgp_table = show_bgp.split('Weight Path')
bgp_table = bgp_table.strip("\n")

with open(output_file, "w") as f:
    for line in bgp_table.splitlines():
        fields = line.split()
        prefix = fields[1]
        as_path = fields[5:-1]
        as_path = " ".join(as_path)
        output_str = "Prefix: {}     as_path: {}\n".format(prefix, as_path)
        f.write(output_str)
