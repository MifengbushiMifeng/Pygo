# coding=utf-8

# practice higher-order-function in Python
def add(x, y, f):
    return f(x) + f(y)


print add(5, -6, abs)


# practice map and reduce

def f(x):
    return x * x


print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def add(x, y):
    return x + y


print reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])


def fn(x, y):
    return 10 * x + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print reduce(fn, map(char2num, '13579'))


def str2int(s):
    def fn(x, y):
        return 10 * x + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# print map(str.capitalize, ['adam', 'LISA', 'barT'])


def correct_name(names):
    return map(str.capitalize, names)


print correct_name(['adam', 'LISA', 'barT'])


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(nums):
    def plus(a, b):
        return a * b

    return reduce(plus, nums)


print prod([2, 3, 4, 5])
