# !/usr/bin/env python
# encoding=utf-8
from collections import defaultdict

d = {'name': 'foo'}

if d.has_key('name'):
    print d['name']
else:
    print 'un-know'

print d.get('name')
print d.get('age', 'un-know')

print '---------------------'

data = [('foo', 10), ('bar', 20), ('foo', 39), ('bar', 49)]

groups = {}
for (key, value) in data:
    if key in groups:
        groups[key].append(value)
    else:
        groups[key] = [value]
print groups

print '---------------------'

groups = {}
for (key, value) in data:
    groups.setdefault(key, []).append(value)
print groups

groups = defaultdict(list)
for (key, value) in data:
    groups[key].append(value)
print groups

numbers = [1, 2, 3]
my_dict = dict([(number, number * 2) for number in numbers])
print my_dict

# do it pythonic
my_dict = {number: number * 2 for number in numbers}
print my_dict

my_dict = {number: number * 2 for number in numbers if number != 2}
print my_dict
