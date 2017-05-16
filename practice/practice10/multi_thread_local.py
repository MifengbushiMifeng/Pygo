# !/usr/bin/env python
# encoding=utf-8

# local threading
from time import sleep
from random import random
from threading import Thread, local

data = local()


def bar():
    print 'called from %s.' % data.v


def foo():
    data.v = str(data.v) + '......'
    bar()


class T(Thread):
    def run(self):
        sleep(random())
        data.v = self.getName()
        sleep(1)
        foo()


T().start()
T().start()
