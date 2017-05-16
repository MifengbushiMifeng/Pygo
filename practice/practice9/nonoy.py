# !/usr/bin/env python
# encoding=utf-8
import os
import shutil
import win32con
import win32api

FOLDER_1 = 'nonoy(4)'
FOLDER_2 = 'r_nonoy(3)'
FOLDER_3 = 'pg_nonoy(2)'
FOLDER_4 = 'tip_nonoy(1)'


def sort_out_files(file_path, out_folder_name):
    full_out_path = file_path + '\\' + out_folder_name
    if os.path.exists(full_out_path):
        shutil.rmtree(full_out_path)
    os.mkdir(full_out_path)
    os.mkdir(full_out_path + '\\' + FOLDER_1)
    # win32api.SetFileAttributes(full_out_path + '\\' + FOLDER_1, win32con.FILE_ATTRIBUTE_NORMAL)
    os.mkdir(full_out_path + '\\' + FOLDER_2)
    # win32api.SetFileAttributes(full_out_path + '\\' + FOLDER_2, win32con.FILE_ATTRIBUTE_NORMAL)
    os.mkdir(full_out_path + '\\' + FOLDER_3)
    # win32api.SetFileAttributes(full_out_path + '\\' + FOLDER_3, win32con.FILE_ATTRIBUTE_NORMAL)
    os.mkdir(full_out_path + '\\' + FOLDER_4)
    # win32api.SetFileAttributes(full_out_path + '\\' + FOLDER_4, win32con.FILE_ATTRIBUTE_NORMAL)
    for root, dirs, files in os.walk(file_path):

        if isinstance(files, list):
            for file in files:
                if file.startswith('a'):
                    # create FOLDER_1 and put the related file into this folder
                    shutil.copyfile(file_path + file, full_out_path + '\\' + FOLDER_1)
                if file.startswith('b') or file.startswith('asda'):
                    pass
                if file.startswith('b'):
                    shutil.copyfile(file_path + '\\' + file, r'C:\3All\S&M\Incidents-bk10\testing')

                if file.startswith('d'):
                    pass


if __name__ == '__main__':
    sort_out_files(
        '',
        'nonoy_2017_05_12')
