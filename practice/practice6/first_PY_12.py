# !/usr/bin/env python
# encoding=utf-8
static_file_path = 'C:\Users\IBM_ADMIN\Desktop\event-log\\test.txt'


def write_file(file_path):
    f = open(file_path, 'w')
    f.write('Hello, Python!')
    f.close()


# write_file(static_file_path)

def write_file2(file_path):
    with open(file_path, 'w') as f:
        f.write('Hello again, Python!')


write_file2(static_file_path)
