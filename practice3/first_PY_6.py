# coding=utf-8
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print x, y

r = move(100, 100, 60, math.pi / 6)
print r


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print power(5)

print power(5, 3)


def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city


enroll('Bob', 'M', 7)

enroll('Adam', 'M', city='Tianjing')


def add_end(L=[]):
    L.append('END')
    return L


print add_end([1, 2, 3])

print add_end()
print add_end()
print add_end()


def add_end_better(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print add_end_better()
print add_end_better()
print add_end_better()
