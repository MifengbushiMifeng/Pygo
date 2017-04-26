# !/usr/bin/env python
# encoding=utf-8
class Fab(object):
    def __init__(self, max_value):
        self.max_value = max_value
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max_value:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()


for i in Fab(5):
    print i
