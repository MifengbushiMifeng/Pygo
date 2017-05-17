# !/usr/bin/env python
# encoding=utf-8
from contextlib import contextmanager, closing


@contextmanager
def demo():
    print '[ Allocate resources ]'
    print ' Code before yield-statement executes in __enter__'
    yield '*** contextmanager demo ***'
    print 'Code after yield-statement executes in __exit__'
    print '[ Free resources ]'


with demo() as value:
    print 'Assigned Value: %s' % value


class ClosingDemo(object):
    def __init__(self):
        self.acquire()

    def acquire(self):
        print 'Acquire resources'

    def free(self):
        print 'Clean up any resources acquired.'

    def close(self):
        self.free()


with closing(ClosingDemo()):
    print 'Using resources.'
