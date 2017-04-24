# !/usr/bin/env python
# encoding=utf-8
"""practice metaclass in python"""
import logging

logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)


# logging.info('n = %d' % n)


# print 10 / n

class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattribute__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
