# !/usr/bin/env python
# encoding=utf-8

# practice multiple return values

test = [1, 2, 3, 4, 5, 3, 2, 23,
        2, 4, 23, 3, 3, 1, 4, 3, 3, 5, 3, 3]
print set(test)
print test.count
print type(test.count)
print max(set(test), key=test.count)

print '~~~~~~~~~~~~~~~~~~'


def return_multi():
    return 1, 2, 3


a, b, c = return_multi()
z = list(return_multi())

print a, b, c
print z

print '~~~~~~~~~~~~~~~~~~'


def test(x, y, z):
    print x, y, z


testDict = {'x': 1, 'y': 2, 'z': 3}
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

print '~~~~~~~~~~~~~~~~~~'

stdcalc = {'sum': lambda x, y: x + y,
           'subtract': lambda x, y: x - y}
print stdcalc['sum'](9, 3)
print stdcalc['subtract'](9, 3)
