# !/usr/bin/env python
# encoding=utf-8

# practice ThreadLocal in python
import threading

# not a good way
global_dict = {}


class Student(object):
    def __init__(self, name):
        self.name = name


def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()


def do_task_1():
    std = global_dict[threading.current_thread()]


def do_task_2():
    std = global_dict[threading.current_thread()]


# using ThreadLocal
local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s).' % (local_school.student, threading.current_thread().name)


def process_thread(name):
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')

t1.start()
t2.start()

t1.join()
t2.join()
