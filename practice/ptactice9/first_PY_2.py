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
