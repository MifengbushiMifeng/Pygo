# !/usr/bin/env python
# encoding=utf-8
try:
    import cPickle as pickle
except ImportError:
    import pickle
# practice pickling and unpickling in Python

d = {'name': 'Bob', 'age': 20, 'score': 88}
d = dict(name='Bob', age=20, score=88);

# print pickle.dumps(d)

f = open('D:\pytest\dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('D:\pytest\dump.txt', 'rb')
d2 = pickle.load(f)
f.close()
print d2
