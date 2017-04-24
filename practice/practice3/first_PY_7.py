# coding=utf-8


# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#
#     return sum


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print calc(1, 2, 3)
print calc()

nums = [1, 2, 3]
print calc(*nums)


def person(name, age, **other):
    print 'name:', name, 'age:', age, 'other:', other


print person('Michael', 30)
print person('Bob', 35, city='Beijing')

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, **kw)


