# coding=utf-8

# practice Generator in Python
# list
L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g

for n in g:
    print n


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


fib(100)


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


g2 = fib2(10)
for i in g2:
    print i


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'print 3'
    yield 5


o = odd()

print o.next()
print o.next()
print o.next()
