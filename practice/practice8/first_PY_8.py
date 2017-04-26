# !/usr/bin/env python
# encoding=utf-8

def fab(nth):
    n, a, b = 0, 0, 1
    fab = []
    while n < nth:
        n = n + 1
        fab.append(b)
        a, b = b, a + b
        # fab.append(a)
    return fab


print fab(5)

print range(0, 10)
print xrange(0, 10)
print list(xrange(0, 10))
