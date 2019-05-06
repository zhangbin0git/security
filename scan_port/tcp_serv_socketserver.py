#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-4 0:23 
# @Author : Mark 
# @Site :  
# @File : tcp_serv_socketserver.py 
# @Software: PyCharm Community Edition

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 9999
ADDR = (HOST, PORT)

class my_request_handler(SRH):
    """请求处理程序"""
    def handle(self):
        print('...connected from: ' + str(self.client_address))
        self.wfile.write(('[{}] {}'.format(ctime(),
            self.rfile.readline().decode()).encode()))

def main():
    tcp_serv = TCP(ADDR, my_request_handler)
    print('wait for connetion .........')
    tcp_serv.serve_forever()

if __name__ == '__main__':
    main()