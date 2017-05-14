# !/usr/bin/env python
# encoding=utf-8

d = {'name': 'Jonathan', 'age': 29, 'email': 'python@py.com'}

for k in d:
    print k, '--->', d[k]

for k, v in d.items():
    print k, '--->', v

print '-----------------------------'

# do it pythonic
for k, v in d.iteritems():
    print k, '--->', v
