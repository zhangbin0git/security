#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 1:49
# @Author  : Zhang Bin
# @Site    : 
# @File    : ssh_command_pxssh.py
# @Software: PyCharm

import pxssh

def send_command(child, cmd):
    # 发送命令
    child.sendline(cmd)
    child.prompt()
    print(child.before)

def connect(user, host, password):
    try:
        child = pxssh.pxssh()
        child.login(host, user, password)
        return child
    except:
        print('[-] Error Conneting')
        exit(0)

if __name__ == '__main__':
    child = connect('root', '', 'toor')
    send_command(child, 'cat etc/shadow |grep root')