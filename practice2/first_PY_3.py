# !/usr/bin/env python
# encoding=utf-8
from collections import deque, defaultdict, OrderedDict

# practice deque in Python
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

dd = defaultdict(lambda: 'N/A')
dd['KEY1'] = 'abc'
print dd['KEY1'], dd['KEY2']

d = dict([('a', '1'), ('b', 2), ('c', 3)])
print d

# order by 'key'
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od

od2 = OrderedDict()
od2['z'] = 1
od2['y'] = 2
od2['x'] = 3
print od2.keys()

