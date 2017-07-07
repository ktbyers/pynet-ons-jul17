#!/usr/bin/env python
# Use named regular expressions
from __future__ import print_function
from __future__ import unicode_literals
import re

with open("show_int_fa4.txt") as f:
    output = f.read()

patterns = {
    "Input": r"(?P<pkts>\d+) packets input, (?P<bytes>\d+) bytes",
    "Output": r"(?P<pkts>\d+) packets output, (?P<bytes>\d+) bytes"
}

for label, pattern in patterns.items():
    match = re.search(pattern, output)
    if match:
        print("\n{}: ".format(label))
        print("Packets: {}".format(match.group('pkts')))
        print("Bytes: {}\n".format(match.group('bytes')))
