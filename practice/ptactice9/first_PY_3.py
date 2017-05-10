# !/usr/bin/env python
# encoding=utf-8

x = [1, 2, 3]
y = [4, 5, 6]

print zip(x, y)

t1 = ('a', 'b', 'b')
t2 = (1, 2, 3)
print zip(t1, t2)

s = '121fdsfecxgfdsfd'
print ';'.join(s)

l = ['name=Jonathan', 'age=27']
print';'.join(l)

name = 'Jonathan'
value = '27'
unknow = (name, value)
print unknow
print type(unknow)
