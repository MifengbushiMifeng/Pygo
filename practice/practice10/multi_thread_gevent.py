# !/usr/bin/env python
# encoding=utf-8
import gevent
from gevent.local import local

# gevent threading

data = local()


def bar():
    print 'called from %s' % data.v


def foo(v):
    data.v = v
    data.v = str(data.v) + '......'
    bar()


g1 = gevent.spawn(foo, '1')
g2 = gevent.spawn(foo, '2')

gevent.joinall([g1, g2])

