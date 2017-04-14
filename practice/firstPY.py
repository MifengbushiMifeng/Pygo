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

testStr = 'Hello, %s'
testStr %= 'world'
print testStr

testStr2 = 'Hi, %s, you have $%d.'
testStr2 %= ('Jonathan', 1000000)
print testStr2
