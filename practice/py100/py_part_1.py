# !/usr/bin/env python
# encoding=utf-8

L = [x + y + z for x in '1234' for y in '1234' for z in '1234' if x != y != z != x]

print L

list1 = ['this', 'is', 'a', 'testing']
for index, item in enumerate(list1):
    print index, item
print '-----------------------------------'
for index, item in enumerate(list1, 10):
    print index, item
print '-----------------------------------'
for i, j in enumerate(('a', 'b', 'c', 'd')):
    print i, j
