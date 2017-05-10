# !/usr/bin/env python
# encoding=utf-8

L = ['Jonathan', 'Zhou', 'Zhao']

L2 = 'Jonathan Zhou Zhao'


def func(aL):
    if isinstance(aL, list):
        return aL[:]
    return [aL]


print func(L)
print func(L2)

str = '123456789'
print str[::-1]

str2 = "this is really a string example....wow!!!";
substr = "is";

print str2.rfind(substr)
print str2.find(substr)

print [m + n for m in 'ABC' for n in 'XYZ']

L = [x + y + z for x in '1234' for y in '1234' for z in '1234' if x != y != z != x]
print L
