# !/usr/bin/env python
# encoding=utf-8
"""practice metaclass in python"""
___author___ = 'Jonathan Zhou'


def fn(self, name='world'):
    print 'Hello, %s.' % name


Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello()


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass


L = MyList()
L.add(1)
print L
