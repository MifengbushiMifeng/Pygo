# coding=utf-8
def func(a, b, c=0, *args, **other):
    print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'other=', other


func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4)
other = {'x': 99}
func(*args, **other)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(5)

# practice slice in python

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]
print L[:3]
print L[-2:]
print L[-2:-1]

L2 = range(100)
print L2[:10:2]
print L2[::5]
