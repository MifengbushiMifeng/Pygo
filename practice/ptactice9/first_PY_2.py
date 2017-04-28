# !/usr/bin/env python
# encoding=utf-8
def foo(*args, **kw):
    print 'args: ', args
    print 'kw: ', kw
    print '-------------------'


if __name__ == '__main__':
    foo(1, 2, 3, 4)
    foo(a=1, b=2, c=3)
    foo(1, 2, 3, 4, 5, a=1, b=2, c=3)
    foo('a', 1, None, a=1, b='2', c=3)


class my_class(object):
    def __init__(self, x, y):
        self._x = x
        self.__y = y


obj = my_class('x', 'y')
print obj._x, obj.__y
