# !/usr/bin/env python
# encoding=utf-8

def fib(n):
    a, b = 0, 1
    result = []
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


# do it pythonic
def fib_gen(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
