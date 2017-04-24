# !/usr/bin/env python
# encoding=utf-8
import random, time, Queue
from multiprocessing.managers import BaseManager

__author__ = 'Jonathan Zhou'

""" taskmanager will start the Queue and register the Queue on the Network """
""" And then write tasks into Queue"""
""" please note this code does't work in windows"""

# the queue to send task
task_queue = Queue.Queue()

# receive the task
result_queue = Queue.Queue()


# the QueueManager that extends BaseManager
class QueueManager(BaseManager):
    pass


# register the task_queue and result_queue into the network
# the 'callable' is the related task
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# bland to 5000 port and the auth is 'abc'
manager = QueueManager(address=('', 5000), authkey='abc')

# start the queue
manager.start()

# get the task from the network
task = manager.get_task_queue()
result = manager.get_result_queue()

# put some task
for i in range(10):
    n = random.randint(0, 10000)
    print 'put task %d...' % n
    task.put(n)

# get the task from result
print 'Try get results'
for i in range(10):
    r = result.get(timeout=10)
    print 'Result: %s' % r

manager.shutdown()
