# coding=utf-8

# define a list in python
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[1]
print classmates[2]
print classmates[-1]
print classmates[-2]
print classmates[-3]

# add item in the end of the array
classmates.append("Adam")
print classmates

# add item in the gave position
classmates.insert(1, 'Jack')
print classmates

# delete the item
deleted = classmates.pop(1)
print deleted
print classmates

classmates[1] = 'Sarah'
print classmates
