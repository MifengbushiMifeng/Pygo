# !/usr/bin/env python
# encoding=utf-8
print 'Hello %(name)s' % {'name': 'Tom'}

print '{greet} from {language}.'.format(greet='Hello world', language='Python')


def h():
    print 'Tester'
    yield 5
    print 'Like Python'


c = h()
c.next()
# c.next()

