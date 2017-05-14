# !/usr/bin/env python
# encoding=utf-8
d = {'name': 'foo'}

if d.has_key('name'):
    print d['name']
else:
    print 'un-know'

print d.get('name')
print d.get('age', 'un-know')
