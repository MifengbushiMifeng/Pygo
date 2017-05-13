# !/usr/bin/env python
# encoding=utf-8

colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print i, '--->', colors[i]

print '---pythonic---'

# do the pythonic
for i, color in enumerate(colors):
    print i, '--->', color

print '--------------------------------'

names = ['Raymond', 'Rachel', 'Matthew', 'Roger', 'Betty']
s = names[0]

for name in names[1:]:
    s += ',' + name

print s

# do it pythonic

print ','.join(names)
