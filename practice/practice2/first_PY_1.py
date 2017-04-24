# !/usr/bin/env python
# encoding=utf-8
import re

# practice regular expression in Python
s = 'ABC\\-001'
s2 = 'ABC\-001'
s3 = r'ABC\-001'

print s, s2, s3

print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

testStr = 'a b  c'
print testStr.split(' ')
print re.split(r'[\s]+', testStr)
testStr = 'a,b;; c    d'
print re.split(r'[\s\,\;]+', testStr)

# Group by ()
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print m.group(0)
print m.group(1)
print m.group(2)
for value in m.groups():
    print value, '--------------------'

print re.match(r'^(\d+)(0*)$', '102300').groups()
print re.match(r'^(\d+?)(0*)$', '201300').groups()

# compile the regular expression
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re.match(re_telephone, '010-12345').groups()
print re.match(re_telephone, '010-8085').groups()
