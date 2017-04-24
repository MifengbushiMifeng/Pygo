# !/usr/bin/env python
# encoding=utf-8

"""practice customize a class"""
__author__ = 'Jonathan Zhou'


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print ('My name is %s.' % self.name)

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 27
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


s = Student('Michael')

print s()

print callable(s)
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')

print s.name
print s.score
print s.age()


# print s.sex

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print Chain().status.user.timeline.list
