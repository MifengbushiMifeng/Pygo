# !/usr/bin/env python
# encoding=utf-8
from collections import deque

names = ['Raymond', 'Rachel', 'Matthew', 'Roger', 'Betty']

print names.pop(0)
print names.insert(0, 'Mark')
print names

# do it pythonic, using deque instead of list for the update action
names_deque = deque(['Raymond', 'Rachel', 'Matthew', 'Roger', 'Betty'])

print names_deque.popleft()
names_deque.appendleft('Mark')
print names_deque

print '-------------------------------'
p = 'vttalk', 'female', 30, 'python@qq.com'
print type(p)
name = p[0]
gender = p[1]
age = p[2]
email = p[3]
print name, gender, age, email

# do it pythonic
n, g, a, e = p
print n, g, a, e
