# !/usr/bin/env python
# encoding=utf-8
import os

L = ['Jonathan', 'Tim', 'Mike']
j, t, m = L
print j, t, m


def file_list(file_path):
    for root, dirs, files in os.walk(file_path):
        print root
        print dirs
        for f in files:
            print f


file_list(r'C:\3All\S&M\Incidents\05.12 - bibit')
