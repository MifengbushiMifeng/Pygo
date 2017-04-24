# coding=utf-8
# First python program
print 'hello, world'
print 'Will learn python hard and quickly'
print '100 + 200 = ', 100 + 200
# name = raw_input('please enter your name:')
# print 'hello,', name

# the logic
a = 100
if a >= 0:
    print a
else:
    print -a

# Shift
print 'I\'m \"OK\"!'

print 10 / 3
print 10.0 / 3

# ASCII
print ord('A')
print chr(65)

print u'\u4e2d'
print u'中'.encode('utf-8')
print len('ABC')

# %d for int; %f for float; %s for string; %x for hex-int
testStr = 'Hello, %s'
testStr %= 'world'
print testStr

testStr2 = 'Hi, %s, you have $%d.'
testStr2 %= ('Jonathan', 1000000)
print testStr2

print '%2d-%02d' % (3, 1)
print '%.3f' % 3.1415926

# If you not sure which %? is the right choice, %s will always works
print 'Age: %s. Gender: %s' % (25, True)

print 'growth rate: %d %%' % 7
