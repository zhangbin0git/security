#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-12 上午12:04
# @Author  : Zhangbin
# @Site    : 
# @File    : default_pages.py
# @Software: PyCharm

# 在ftp中查找默认网页

import ftplib

def return_default(ftp):
    try:
        # 列出目录中所有的文件
        dir_list = ftp.nlst()
    except Exception as e:
        dir_list = []
        print('[-] Could not list directory contents.')
        print('[-] Skipping to next target')
        return
    ret_list = []
    for filename in dir_list:
        fn = filename.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + filename)
            ret_list.append(filename)
    return ret_list

if __name__ == '__main__':
    host = ''
    user_name = ''
    password = ''
    ftp = ftplib.FTP(host)
    ftp.login(user_name, password)
    return_default(ftp)