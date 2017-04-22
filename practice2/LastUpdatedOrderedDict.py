# !/usr/bin/env python
# encoding=utf-8
from collections import OrderedDict

# practice OrderDict in Python

__author__ = 'Jonathan Zhou'


# 'LastUpdatedOrderedDict' is an FIFO(first in first out) dict
# When the max size > capacity, will delete the first in key
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)

        OrderedDict.__setitem__(self, key, value)
