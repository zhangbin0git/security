#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-2 0:03 
# @Author : Mark 
# @Site :  
# @File : nmap_scan.py 
# @Software: PyCharm Community Edition'

import optparse
import nmap


def nmap_scan(tgt_host, tgt_port):
    """使用nmap扫描端口"""
    nm_scan = nmap.PortScanner()
    nm_result = nm_scan.scan(tgt_host, tgt_port)
    print(nm_result)
    # state = nm_scan[tgt_host]['tcp'][int(tgt_port)]['state']
    # print('[*] ' + tgt_host + ' tcp ' + tgt_port + ' ' + state)


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
        for port in tgt_ports:
            nmap_scan(tgt_host, port)

# if __name__ == '__main__':
#     main()

nmap_scan('127.0.0.1', '9999')