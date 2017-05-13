# !/usr/bin/env python
# encoding=utf-8

f = open('test.txt')
try:
    data = f.read()
finally:
    f.close()

# do it pythonic
with open('test.txt') as f:
    data = f.read()
