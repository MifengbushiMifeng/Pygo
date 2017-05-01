# !/usr/bin/env python
# encoding=utf-8

x = [1, 2, 3]
y = [4, 5, 6]

print zip(x, y)

t1 = ('a', 'b', 'b')
t2 = (1, 2, 3)
print zip(t1, t2)

s = '121fds fecx gfdsfd'
print ''.join(s)

name = 'Jonathan'
value = '27'
unknow = (name, value)
print unknow
print type(unknow)
