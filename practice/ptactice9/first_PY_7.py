# !/usr/bin/env python
# encoding=utf-8

import os


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        for file in files:
            print file  # 当前路径下所有非目录子文件


file_name(r'C:\3All\S&M\Incidents\05.12 - bibit')
