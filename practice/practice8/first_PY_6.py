# !/usr/bin/env python
# encoding=utf-8
import time
import calendar

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

dict2 = dict1
dict3 = dict1.copy()

dict1['user'] = 'root'
dict1['num'].remove(1)

print dict1, dict1.get('user'), dict1['user']
print dict2
print dict3

print dict1.items()

localtime = time.localtime(time.time())
print time.asctime(localtime)
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

cal = calendar.month(2017, 4)
print cal

# practice list comprehensions
l = [m + n for m in 'ABC' for n in 'XYZ']
print l

l2 = ['Hello', 'World', 18, 'Apple', 'IBM', None]
l3 = [value.lower() for value in l2 if isinstance(value, str)]
print l3
