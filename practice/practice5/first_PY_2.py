# coding=utf-8
arr = [36, 15, 12, 9, 3]
print sorted(arr)


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x == y:
        return 0
    if x < y:
        return 1


print sorted(arr, reversed_cmp)

arr_str = ['bob', 'about', 'Zoo', 'Credit']


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(arr_str, cmp_ignore_case)


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print calc_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)

print f()
