# coding=utf-8
from collections import Iterable

# practice iteration in python

# iteration of key for dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key

# iteration of value for dict
for value in d.itervalues():
    print value

# iteration of key/value for dict
for k, v in d.iteritems():
    print k, v

for ch in 'ABC':
    print ch

# how to judge an object is iterable
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
