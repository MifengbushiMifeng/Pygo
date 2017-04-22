# !/usr/bin/env python
# encoding=utf-8
from collections import namedtuple

# practice batteries included in Python

p = (1, 2)

for n in p:
    print n

print p

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)

print p.x, p.y
print type(p)
print isinstance(p, Point)
