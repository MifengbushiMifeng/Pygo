# !/usr/bin/env python
# encoding=utf-8
from gevent import monkey
import gevent
import urllib2

monkey.patch_all()


def f(url):
    print 'GET: %s' % url
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '%d bytes received from %s.' % (len(data), url)


gevent.joinall([

    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://github.com/'),

])
