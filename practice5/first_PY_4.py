# coding=utf-8
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'Begin call %s:' % func.__name__
        func(*args, **kw)

        print 'End call %s:' % func.__name__

    return wrapper


@log
def go():
    print 'Python GO!'


go()


def log2(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text == '':
                print '%s strat:' % func.__name__
            else:
                print '%s %s:' % (text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return decorator


@log2()
def f1():
    print 'F1 is running'


@log2('execute')
def f2():
    print 'F2 is running'


f1()
f2()
