# !/usr/bin/env python
# encoding=utf-8

L = [i * i for i in range(5)]
print L

index = 0

for data in L:
    print data, ':', index
    index += 1

for index, data in enumerate(L):
    print index, ':', data

print '-----------------------'

L2 = [1, 2, 3, 4]
for item in L2[::-1]:
    print item
print reversed(L2)
for item in reversed(L2):
    print item

for i in L2:
    if i == 3:
        print 'there is a THREE'

if any(i == 3 for i in L2):
    print 'there is a ThREE aga'
