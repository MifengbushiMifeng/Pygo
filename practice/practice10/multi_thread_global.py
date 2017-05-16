# !/usr/bin/env python
# encoding=utf-8
from time import sleep
from random import random
from threading import Thread, local


# global threading
def bar1():
    global v
    print 'calleddddd from %s' % v


def foo1():
    global v
    v = v + '......'
    print 'calleddddd from %s' % v


class T1(Thread):
    def run(self):
        global v
        sleep(random())
        v = self.getName()
        sleep(1)
        foo1()


T1().start()
T1().start()
