# !/usr/bin/env python
# encoding=utf-8
"""practice metaclass in python"""
import logging

___author___ = 'Jonathan Zhou'


def Afunc():
    try:
        print 'try...'
        r = 10 / 0
        print 'result:', r
    except ZeroDivisionError, e:
        print 'except:', e
    finally:
        print 'finally...'
    print 'END'


# Afunc()


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar(0)
    except StandardError, e:
        logging.exception(e)
    finally:
        print 'finally...'


main()
