from __future__ import print_function

f = open("show_ip_bgp.txt")
output = f.readlines()

for line in output:
    line = line.strip()
    if line and '*' in line[0]:
        fields = line.split()
        prefix = fields[1]
        as_path = fields[5:-1]
#        print(prefix)
        print(as_path)
        #break
