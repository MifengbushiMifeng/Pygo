# !/usr/bin/env python
# encoding=utf-8

age = 18

if 18 < age < 60:
    print 'young man'

gender = 'male'
if gender == 'male':
    text = 'nan'
else:
    text = 'nv'

print text

text = 'nan' if gender == 'male' else 'nv'

print text
