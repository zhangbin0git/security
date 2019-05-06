#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-3 23:27 
# @Author : Mark 
# @Site :  
# @File : udp_serv_py3.py 
# @Software: PyCharm Community Edition

import socket
from time import ctime

def udp_server():
    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    udp_ser_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_ser_sock.bind(ADDR)

    while True:
        print('waiting for message...')
        data, addr = udp_ser_sock.recvfrom(BUFSIZ)
        udp_ser_sock.sendto('[{}] {}'.format(ctime(), data.decode()).encode(), addr)
        print('...received from and returned to:' + str(addr))
    udp_ser_sock.close()

if __name__ == '__main__':
    udp_server()