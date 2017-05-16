# !/usr/bin/env python
# encoding=utf-8

import sys

x = 1001
print sys.getrecursionlimit()

sys.setrecursionlimit(x)

print sys.getrecursionlimit()

x = 1
print sys.getsizeof(x)

print '~~~~~~~~~~~~~~~~~~~~~~~~'


class FileSystem(object):
    def __init__(self, files, folders, devices):
        self.files = files
        self.folders = folders
        self.devices = devices


print sys.getsizeof(FileSystem)


class FileSystem1(object):
    __slots__ = ['files', 'folders', 'devices']

    def __init__(self, files, folders, devices):
        self.files = files
        self.folders = folders
        self.devices = devices


print sys.getsizeof(FileSystem1)

t1 = (1, 2, 3)
t2 = (10, 20, 30)
print dict(zip(t1, t2))

print ('http://www.google.com'.startswith(('http', 'https')))
print ('https://www.google.com'.startswith(('http', 'https')))
