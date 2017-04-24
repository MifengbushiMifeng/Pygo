# coding=utf-8
import functools

# practice partial function in Python
print int('13')
print int('13', base=16)


def int2(num, base=2):
    return int(num, base)


print int2('1101010101010')

int_new = functools.partial(int, base=2)
print int_new('1001010101010')
print int_new('1000', base=10)

max_new = functools.partial(max, 10)
print max_new(1, 2, 3, 9)
