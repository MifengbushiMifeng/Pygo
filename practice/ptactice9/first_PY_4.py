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
