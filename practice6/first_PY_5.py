# !/usr/bin/env python
# encoding=utf-8

"""practice customize a class"""
__author__ = 'Jonathan Zhou'


class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student Object: name is %s' % self.__name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25


s = Student('Michael')

print s
print s.score, s.age()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# for n in Fib():
#     print n

f = Fib()
print f[0:5]
