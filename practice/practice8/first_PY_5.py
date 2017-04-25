# !/usr/bin/env python
# encoding=utf-8
import math
import random

print math.ceil(4.1)
print cmp(1, 2)
print math.exp(1)
print math.log(100)

print '-------------------------------------'

print random.choice(range(10))
print random.randrange(1, 10, 2)
list = [20, 16, 10, 5];
random.shuffle(list)
print list
print random.uniform(1, 5)

str1 = u'Hello\u0020World !'

print str1

str2 = 'jonathan'
if isinstance(str2, str):
    print str2.capitalize()
    print str2.center(20, '-')
    print str2.count('n')
    print str2.endswith('than')
    print str2.find('na')
    print str2.find('z')
    print str2.index('na')
    # print str2.index('z')
    print str2.isalnum()
    print 'asdsa!?!?'.isalnum()
    print 'acb'.isalpha()
    print 'ac2'.isalpha()
    print '121212'.isdigit()

str11 = u"23443434"
print str11.isdecimal()

print '-------------------------------------'

str3 = "hha"
seq = ["a", "b", "c"]
print str3.join(seq)

print '-------------------------------------'

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];

print aList + bList

aList.extend(bList)

print "Extended List : ", aList
