#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-3 0:33 
# @Author : Mark 
# @Site :  
# @File : tcp_clnt_py3.py
# @Software: PyCharm Community Edition

import socket

def clinet():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    # 声明socket类型，同时生成链接对象
    tcp_cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_cli_sock.connect(ADDR)

    while True:
        data = input('> ')
        if not data:
            break
        tcp_cli_sock.send(data.encode('utf-8'))
        data = tcp_cli_sock.recv(BUFSIZ)
        if not data:
            break
        print('recv:' + data.decode('utf-8'))
    tcp_cli_sock.close()

if __name__ == '__main__':
    clinet()
