#!/usr/bin/env python
from __future__ import print_function

#### READ ####
f = open("my_file.txt")
print("\nLoop directly over file")
print("-" * 60)
for line in f:
    print(line.strip())
print("-" * 60)

f.seek(0)
my_content = f.readlines()
print("\nUse readlines method")
print("-" * 60)
for line in my_content:
    print(line.strip())
print("-" * 60)

f.seek(0)
my_content = f.read()
print("\nUse read + splitlines")
print("-" * 60)
for line in my_content.splitlines():
    print(line)
print("-" * 60)
f.close()

with open("my_file.txt") as f:
    print("\nUse with and loop over file")
    print("-" * 60)
    for line in f:
        print(line.strip())
    print("-" * 60)


#### WRITE ####
print("\nWriting file.")
f = open("new_file.txt", "w")
f.write('whatever2\n')
f.close()

#### APPEND ####
print("\nAppending file.")
with open("new_file.txt", "a") as f:
    f.write('something else\n')
print()
