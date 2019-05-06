#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-6 11:42 
# @Author : Mark 
# @Site :  
# @File : ssh_command.py
# @Software: PyCharm Community Edition

# 实现与程序交互、等待预期的屏幕输出，并作出反应
import pexpect

# 系统返回的提示符号,常量
PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    """向ssh发送命令"""
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def connet(user, host, password):
    # SSH返回的信息
    ssh_newkey = 'Are you sure you want to continue conneting'
    conn_str = 'ssh ' + user + '@' + host
    child = pexpect.spawn(conn_str)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[p|P]assword:')



