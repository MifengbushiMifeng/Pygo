# !/usr/bin/env python
# encoding=utf-8
import os
import stat

print os.name
# print os.environ
# print os.getenv('PATH')

print os.path.abspath('.')

os.path.join('D:\pytest', 'testdir')
os.mkdir('D:\pytest\\testdir')
os.chmod('D:\pytest\\testdir', stat.S_IWRITE)
os.chmod('D:\pytest', stat.S_IWRITE)
os.chmod('D:\pytest', stat.S_IWRITE)

os.rmdir('D:\pytest\\testdir')

print os.path.split('/Users/michael/testdir/file.txt')
print os.path.splitext('/path/to/file.txt')

os.rename('D:\pytest\\test.txt', 'D:\pytest\\test.py')
os.remove('D:\pytest\\test.py')

# print os.listdir('D:\jars')
print [x for x in os.listdir('D:\jars')]


pass
# 练习：编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
#
# $ python search.py test
# unit_test.log
# py/test.py
# py/test_os.py
# my/logs/unit-test-result.txt
