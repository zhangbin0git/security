#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-4 10:19 
# @Author : Mark 
# @Site :  
# @File : tcp_serv_tw.py 
# @Software: PyCharm Community Edition
# Twisted 网络框架实例

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class ts_serv_protocol(protocol.Protocol):
    def connectionMade(self):
        """当客户端连接服务器时，执行"""
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: ' + clnt)

    def dataReceived(self, data):
        """服务器接收到客户端的数据时调用"""
        self.transport.write(('[{}] {}'.format(ctime(), data.decode())).encode())

# 创建协议工厂
factory = protocol.Factory()
factory.protocol = ts_serv_protocol
print('waiting for connection...')
# 监听端口
reactor.listenTCP(PORT, factory)
reactor.run()

