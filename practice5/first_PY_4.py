# coding=utf-8
import time


# practice decorator in Python
def now():
    print time.strftime('%Y-%m-%d', time.localtime(time.time()))


f = now
f()
print f.__name__
