#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-19 22:49
# @Author  : Zhang Bin
# @Site    : 
# @File    : return_dir.py
# @Software: PyCharm

import os
import winreg
def return_dir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recy in dirs:
        if os.path.isdir(recy):
            return recy
    return None

def sid2user(sid):
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList\\'+ sid)
        print(key)
        (value, t) = winreg.QueryValueEx(key, 'ProfileImagePath')
        print(value, t)
        user = value.split('\\')[-1]
        return user
    except:
        return sid

def find_recycled(recycledir):
    dirlist = os.listdir(recycledir)
    for sid in dirlist:
        files = os.listdir(recycledir + sid)
        user_name = sid2user(sid)
        print('\n[*] listing files for user: ' + str(user_name))
        for file in files:
            print('[+] found file: ' + str(file))

def main():
    rec = return_dir()
    find_recycled(rec)

if __name__ == '__main__':
    main()