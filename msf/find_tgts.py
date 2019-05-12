#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-12 上午1:16
# @Author  : Zhangbin
# @Site    : 
# @File    : find_tgts.py
# @Software: PyCharm
# nmap 扫描
import nmap

def find_tgts(sub_net):
    nmscan = nmap.PortScanner()
    nmscan.scan(sub_net, '445')
    tgt_hosts = []
    for host in nmscan.all_hosts():
        if nmscan[host].has_tcp(445):
            state = nmscan[host]['tcp'][445]['state']
            if state == 'open':
                print('[+] Found target host: ' + host)
                tgt_hosts.append(host)
    return tgt_hosts