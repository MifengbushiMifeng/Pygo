# !/usr/bin/env python
# encoding=utf-8
import time, sys, Queue
from multiprocessing.managers import BaseManager

__author__ = 'Jonathan Zhou'


# create the QueueManager
class QueueManager(BaseManager):
    pass


# As this QueueManager only can get queue from network, so only need the task name when registering
QueueManager.register('get_task_queue')
QueueManager.register("get_result_queue")

# Connect to the queue server
server_addr = '127.0.0.1'
print 'Connect to server %s' % server_addr

# Please note the port and then auth ket should be same with the server
m = QueueManager(address=(server_addr, 5000), authkey='abc')
m.connect()

# get the queue
task = m.get_task_queue()
result = m.get_result_queue()

# get task from 'task' queue and put into 'result' queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print 'run task %d * %d' % (n, n)
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print 'task queue is empty'

print 'worker exit'
