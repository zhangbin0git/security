#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-3 0:10 
# @Author : Mark 
# @Site :  
# @File : tcp_serv_py3.py
# @Software: PyCharm Community Edition

import socket
from time import ctime

def server():
    """开启指定端口"""
    HOST = ''
    PORT = 9999
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcp_ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定要监听的端口
    tcp_ser_sock.bind(ADDR)
    # 开始监听 表示可以使用五个链接排队
    tcp_ser_sock.listen(5)

    while True:
        # tcp_cli_sock是客户端链接过来而在服务端为期生成的一个链接实例
        # 等待链接,多个链接
        print('waiting for connection...')
        tcp_cli_sock, addr = tcp_ser_sock.accept()
        print('...connected from:', addr)
        while True:
            try:
                # 接收数据
                data = tcp_cli_sock.recv(BUFSIZ)
                if data == 'exit' or not data:
                    break
                print('recive:', data.decode())  # 打印接收到的数据
                tcp_cli_sock.send(("[{}] {}".format(ctime(),
                    data.decode().upper())).encode())
            except ConnectionResetError as e:
                print('关闭了正在占线的链接！')
                break
        tcp_cli_sock.close()
    tcp_ser_sock.close()

if __name__ == '__main__':
    server()

