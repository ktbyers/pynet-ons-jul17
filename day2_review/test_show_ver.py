from __future__ import print_function

f = open("show_version.txt")
output = f.readlines()

for line in output:
    if 'Processor board ID' in line:
        fields = line.split("Processor board ID")
        serial_num = fields[1].strip()
        print(serial_num)
