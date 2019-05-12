#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 1:49
# @Author  : Zhang Bin
# @Site    : 
# @File    : ssh_command_pxssh.py
# @Software: PyCharm

from pexpect import pxssh

def send_command(child, cmd):
    # 发送命令
    child.sendline(cmd)
    child.prompt()
    print(child.before.decode('utf-8'))

def connect(user, host, password):
    try:
        child = pxssh.pxssh()
        child.login(host, user, password)
        return child
    except:
        print('[-] Error Conneting')
        exit(0)

if __name__ == '__main__':
    # child = connect('root', '127.0.0.1', 'toor')
    child = connect('zb', '192.168.1.2', 'zlx520')
    # send_command(child, 'cat /etc/shadow | grep root')
    send_command(child, 'dir')