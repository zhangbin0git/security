#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-1 23:08 
# @Author : Mark 
# @Site :  
# @File : scan_port.py 
# @Software: PyCharm Community Edition

# 做端口扫描

import optparse
import socket
import threading

# 信息锁
screen_lock = threading.Semaphore(value=1)

def conn_scan(tgt_host, tgt_port):
    """连接并返回端口信息"""
    try:
        conn_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn_skt.connect((tgt_host, tgt_port))
        conn_skt.send('who are you'.encode('utf-8'))
        result = conn_skt.recv(1024)
        screen_lock.acquire()
        print('[+] {} tcp open'.format(tgt_port))
        print('[+] {}'.format(str(result.decode())))
    except:
        screen_lock.acquire()
        print('[-] {} tcp closed'.format(tgt_port))
    finally:
        screen_lock.release()
        conn_skt.close()

def port_scan(tgt_host, tgt_ports):
    """对指定地址的多个端口进行扫描"""
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except:
        print('[-] Cannot resolve {}: Unknown host'.format())
        return
    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)
        print('\n[+] Scan Results for: {}'.format(tgt_name[0]))
    except:
        print('\n[+] Scan Results for: {}'.format(tgt_ip))
    # 设置默认超时时间
    socket.setdefaulttimeout(1)
    for port in tgt_ports:
        t = threading.Thread(target=conn_scan, args=(tgt_ip, int(port)))
        t.start()

def main():
    """主程序"""
    parser = optparse.OptionParser('usage %prog '
                                   '-H <target host> -P <target port>')
    parser.add_option('-H', dest='tgt_host', type='string',
                      help='specify target host')
    parser.add_option('-P', dest='tgt_ports', type='string',
                      help='specify target port[s] separated by comma')
    (option, args) = parser.parse_args()
    tgt_host = option.tgt_host
    tgt_ports = str(option.tgt_ports).split(',')
    if tgt_host == None or tgt_ports[0] == None:
        print(parser.usage)
        exit(0)
    else:
        port_scan(tgt_host, tgt_ports)

if __name__ == '__main__':
    main()

