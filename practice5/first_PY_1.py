# coding-utf-8
# practice filter in Python
def is_odd(n):
    return n % 2 == 1


print filter(is_odd, [1, 2, 3, 4, 5, 7, 9, 10, 11])

print is_odd(2)


# def not_empty(s):
#     return s and s.strip()
#
#
# # print not_empty()
# print not_empty('   ')

def not_empty(s):
    return s and s.strip()


print not_empty('  ')

print filter(not_empty, ['A', '', 'B', None, 'C', '  '])


def is_prime(num):
    if num == 2:
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


print filter(is_prime, [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 23])
