# !/usr/bin/env python
# encoding=utf-8

from multiprocessing import Process
import os, time, random


def r():
    print 'run method.'


if __name__ == '__main__':
    print 'main process run...'

    p1 = Process()
    p2 = Process()

    p1.run = r
    p2.run = r

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print 'main process runned all lines...'
