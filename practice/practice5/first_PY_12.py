# coding=utf-8

import types

print type(123)

print type('str')

print type(None)

print type('abc') == types.StringType
print type([]) == types.ListType

print dir('str')

# len() is equals __len__()
print len('ABC')
print 'ABC'.__len__()


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


myObj = MyObject()
print hasattr(myObj, 'x')

print hasattr(myObj, 'y')

setattr(myObj, 'y', 19)

print hasattr(myObj, 'y')

print getattr(myObj, 'y')

print myObj.y

# getattr(myObj, 'z') Will got an Attribute error exception

print getattr(myObj, 'z', 404)

print hasattr(myObj, 'power')

fn = getattr(myObj, 'power')

print fn()
