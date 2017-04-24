# !/usr/bin/env python
# encoding=utf-8

def application(environ, start_reapsonse):
    start_reapsonse('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
