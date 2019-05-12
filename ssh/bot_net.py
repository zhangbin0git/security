#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-11 下午10:49
# @Author  : Zhangbin
# @Site    : 
# @File    : bot_net.py
# @Software: PyCharm

# 僵尸网络

import optparse
from pexpect import pxssh

bot_net =[]

class Client:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            con = pxssh.pxssh()
            con.login(self.host, self.user, self.password)
            return con
        except Exception as e:
            print(e)
            print('[-] Error Connecting')

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before.decode('gbk')

def add_client(host, user, password):
    client = Client(host, user, password)
    bot_net.append(client)

def send_bot_net_command(cmd):
    for client in bot_net:
        out_put = client.send_command(cmd)
        print('[+] output from ' + client.host)
        print('[+] ' + out_put)

if __name__ == '__main__':
    add_client('127.0.0.1', 'root', 'toor')
    send_bot_net_command('uname -v')
    send_bot_net_command('cat /etc/issue')
