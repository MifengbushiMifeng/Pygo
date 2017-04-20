# !/usr/bin/env python
# encoding=utf-8

# f = open('C:\Users\IBM_ADMIN\Desktop\event-log\\test.txt', 'r')
# print f.name
# print f.read()
import codecs

filePath = 'C:\Users\IBM_ADMIN\Desktop\event-log\\test.txt'


def read_file(filePath):
    f = open(filePath, 'r')
    print f.name
    print f.read()
    f.close()


# read_file(filePath)


def read_file2(filePath):
    with open(filePath, 'r') as f:
        print f.read()


# read_file2(filePath)


def read_file3(filePath):
    with open(filePath, 'r') as f:
        for line in f.readlines():
            print line.strip()


# read_file3(filePath)

def read_file4(filePath):
    f = open(filePath, 'rb')
    u = f.read().decode('gbk')
    print u


# read_file4(filePath)

def read_file5(filePath):
    with codecs.open(filePath, 'r', 'gbk') as f:
        print f.read()


read_file5(filePath)
