#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-3 23:34 
# @Author : Mark 
# @Site :  
# @File : udp_clnt_py3.py 
# @Software: PyCharm Community Edition

import socket

def udp_client():
    HOST = '127.0.0.1'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    udp_cli_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input('> ')
        if not data:
            break
        udp_cli_sock.sendto(data.encode(), ADDR)
        data, ADDR = udp_cli_sock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data.decode())
        print(ADDR)
    udp_cli_sock.close()

if __name__ == '__main__':
    udp_client()