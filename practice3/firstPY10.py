# coding=utf-8
import os

# practice List Comprehensions in python
# generate list : [1*1, 2*2...,10*10]
L = [x * x for x in range(1, 11)]
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print L
print L2

L3 = [m + n for m in 'ABC' for n in 'XYZ']
print L3

L4 = [m + n for m in 'ABCD' for n in 'ABCD']
print L4

list = [d for d in os.listdir('D:\Cisco')]
print list
