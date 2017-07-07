#!/usr/bin/env python

import json

my_list = range(10)
my_list.append('whatever')
my_list.append('some thing')

my_dict = {
  'key1': 'val1',
  'key2': 'val2',
  'key3': 'val3'
}
my_dict['key4'] = my_list
my_dict['key5'] = False

print my_dict
print json.dumps(my_dict)

with open("my_file.json", "w") as f:
    json.dump(my_dict, f)
