#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-4 12:15 
# @Author : Mark 
# @Site :  
# @File : tcp_clnt_tw.py 
# @Software: PyCharm Community Edition

from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PORT = 21567

class ts_clnt_protocol(protocol.Protocol):
    def send_data(self):
        # 添加自建函数，实现相关功能
        data = input('> ')
        if data:
            self.transport.write(data.encode('utf-8'))
        else:
            # 关闭套签字
            self.transport.loseConnection()

    def connectionMade(self):
        # 当客户端连接服务器时，执行
        self.send_data()

    def dataReceived(self, data):
        # 客户端接收到服务端的数据时调用
        print(data.decode())
        self.send_data()

class ts_clnt_factory(protocol.ClientFactory):
    """客户端工厂"""
    protocol = ts_clnt_protocol
    # 调用此方法停止reactor
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT,  ts_clnt_factory())
reactor.run()
