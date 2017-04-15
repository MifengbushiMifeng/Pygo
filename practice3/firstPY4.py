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
