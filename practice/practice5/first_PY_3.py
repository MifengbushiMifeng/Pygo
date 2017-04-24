# coding=utf-8

# practice return function in Python
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print f1(), f2(), f3()


def count2():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g()

        fs.append(f(i))
    return fs


f4, f5, f6 = count2()
print f4, f5, f6

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f7 = lambda x: x * x

print f7(6)


def build(x, y):
    return lambda: x * x + y * y


print build(1, 3)()
