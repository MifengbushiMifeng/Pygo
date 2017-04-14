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
