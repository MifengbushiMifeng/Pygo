# !/usr/bin/env python
# encoding=utf-8

# f = open('C:\Users\IBM_ADMIN\Desktop\event-log\\test.txt', 'r')
# print f.name
# print f.read()
import codecs

file_Path = 'C:\Users\IBM_ADMIN\Desktop\event-log\\test.txt'


def read_file(file_path):
    f = open(file_path, 'r')
    print f.name
    print f.read()
    f.close()


# read_file(filePath)


def read_file2(file_path):
    with open(file_path, 'r') as f:
        print f.read()


# read_file2(filePath)


def read_file3(file_path):
    with open(file_path, 'r') as f:
        for line in f.readlines():
            print line.strip()


# read_file3(filePath)

def read_file4(file_path):
    f = open(file_path, 'rb')
    u = f.read().decode('gbk')
    print u


# read_file4(filePath)

def read_file5(filePath):
    with codecs.open(filePath, 'r', 'gbk') as f:
        print f.read()


read_file5(file_Path)
