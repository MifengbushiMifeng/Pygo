# !/usr/bin/env python
# encoding=utf-8

class DummyResource():
    def __init__(self, tag):
        self.tag = tag
        print 'Resource [%s].' % tag

    def __enter__(self):
        print '[Enter %s]: Allocate resource.' % self.tag
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '[Exut %s]: Free resource.' % self.tag
        if exc_tb is None:
            print '[Exit %s]: Exited without exception.' % self.tag
        else:
            print '[Exit %s]: Exited with exception raised.' % self.tag
            return False


with DummyResource('Normal'):
    print '[with-body] Run without exceptions.'
print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
with DummyResource('with-Exception'):
    print '[with-body] Run with exception.'
    raise Exception
    print '[with-body] Run with exception. Failed to finish statement-body!'
