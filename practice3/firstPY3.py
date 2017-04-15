# coding=utf-8

# define a tuple in python
# tuple is very same with list, unless the tuple can not be modified after initial
classmates = ('Michael', 'Bob', 'Tracy')
print classmates

changedTuple = ('a', 'b', ['A', 'B'])
print changedTuple

changedTuple[2][0] = 'X'
changedTuple[2][0] = 'Y'

print changedTuple

# Logic
age = 3
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >= 6:
    print 'your age is', age
    print 'teenager'
else:
    print 'kid'

print '####################'

# Loop
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

print range(4)

sum = 0
for x in range(101):
    sum += x
print sum

sum2 = 0
n = 99
while n >= 0:
    sum2 += n
    n -= 2
print sum2
