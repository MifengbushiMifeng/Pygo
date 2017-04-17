# coding=utf-8

# practice function in python
print abs(100), abs(-20)

print cmp(1, 2), cmp(2, 1), cmp(3, 3)

print int('123'), int(12.34), float('12.34'), str(1.23), unicode(100), bool(2), bool('')

funcA = abs
print funcA(-3)


# define my first function in python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print my_abs(-103)
print my_abs('A')


def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print my_abs2(-333)
print my_abs2('A')
