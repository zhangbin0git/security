#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-4 0:33 
# @Author : Mark 
# @Site :  
# @File : tcp_clnt_socketserver.py 
# @Software: PyCharm Community Edition

import socket

def client():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    while True:
        tcp_cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_cli_sock.connect(ADDR)
        data = input('> ')
        if not data:
            break
        tcp_cli_sock.send((data + '\n').encode())
        data = tcp_cli_sock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode())
        tcp_cli_sock.close()

if __name__ == '__main__':
    client()