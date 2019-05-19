#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-12 下午9:43
# @Author  : Zhangbin
# @Site    : 
# @File    : val2addr.py
# @Software: PyCharm
# 将数值转为mac地址
# 其他方法list(bytes('\x00\x00\x00\x00\x00\x00\x00\x11', 'ascii'))

def var2addr(val):
    addr = ''
    for ch in val:
        addr += ('%02x '% ord(ch))
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr

def var2addr_v1(val):
    addr = ''
    for ch in list(bytes(val, 'ascii')):
        addr += ('%02x '% ch)
    addr = addr.strip(' ').replace(' ', ':')[0:17]
    return addr
