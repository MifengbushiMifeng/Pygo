# coding=utf-8

# practice of dict(map) in python
dictScores = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print dictScores['Michael']

dictScores['Adam'] = 67
print dictScores['Adam']

if 'Adam' in dictScores:
    print 'Adam is available'

if 'Thomas' in dictScores:
    print 'Thomas is available'
else:
    print 'Thomas is unavailable'

print dictScores.get('Thomas')
print dictScores.get('Thomas', -1)

bob = dictScores.pop('Bob')
print bob
print dictScores

# practice of set in python
# s = {1, 2, 3, 3, 4}

s = set([1, 2, 3, 4])
print s

s.add(5)
s.add(4)

print s
s.remove(4)
print s

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2
