# !/usr/bin/env python
# encoding=utf-8

# practice multi-processing in Python

from multiprocessing import Pool

import os, time, random


def log_time_task(name):
    print 'Run task %s (%s).' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool(5)
    for i in range(5):
        p.apply_async(log_time_task, args=(i,))
    print 'Waiting for all sub-processes done...'
    p.close()
    p.join()
    print 'All sub-processes done.'
