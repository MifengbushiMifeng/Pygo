# !/usr/bin/env python
# encoding=utf-8

L = [x + y + z for x in '1234' for y in '1234' for z in '1234' if x != y != z != x]

print L
