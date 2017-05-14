# !/usr/bin/env python
# encoding=utf-8

# '----- test block -----'


def process(i):
    print i


flagfound = False
mylist = [1, 2, 3, 4, 5]
theflag = 3
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(i)
if not flagfound:
    raise ValueError('List argument missing terminal flag.')

# '----- test block -----'

# do it pythonic
for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    raise ValueError('List argument missing terminal flag.')
