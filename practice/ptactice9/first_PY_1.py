# !/usr/bin/env python
# encoding=utf-8

class dummy_resource():
    def __init__(self, tag):
        self.tag = tag
        print 'Resource [%s]' % tag

    def __enter__(self):
        print '[Enter %s]: Allocate resource.' % self.tag
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '[Exit %s]: Free resource.' % self.tag
        if exc_tb is None:
            print '[Exit %s]: without exception.' % self.tag
        else:
            print '[Exit %s]: Exited with exception raised.' % self.tag
            return False
