#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 1:21
# @Author  : Zhang Bin
# @Site    : 
# @File    : defaultepages.py
# @Software: PyCharm
# 发现ftp下的默认网页
import ftplib
def return_default(ftp):
    try:
        # 列出目录中的文件
        dir_list = ftp.nlst()
    except:
        dir_list = []
        print('[-] Could not list directory contents')
        print('[-] Skipping to next target')
        return
    ret_list = []
    for line in dir_list:
        fn = line.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print('[+] Found default page: ' + line)
            ret_list.append(line)

host = ''
user = ''
password = ''
ftp = ftplib.FTP(host)
ftp.login(user, password)
return_default(ftp)

