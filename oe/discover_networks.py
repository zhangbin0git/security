#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-16 11:17 
# @Author : Mark 
# @Site :  
# @File : discover_networks.py 
# @Software: PyCharm Community Edition
# 发现电脑连过的无线及mac地址

import winreg
from val2addr import var2addr

def print_nets():
    net = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList" \
          r"\Signatures\Unmanaged"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print('\n[*] Networks you have joined.')
    for i in range(100):
        try:
            # 该函数用于枚举获取key下的subkey，返回类型为handle(操作句柄)
            guid = winreg.EnumKey(key, i)
            netkey = winreg.OpenKey(key, str(guid))
            # winreg.EnumValue(key, index)index用于指定要获取键的整数。此函数返回一
            # 个元组(name, data, type), 其中name是值的名称, data是保存值数据的对象,
            # 而type是指定值数据类型的整数。
            # 网关mac
            (name, mac, t) = winreg.EnumValue(netkey, 4)
            # 无线ssid
            (name, ssid, t) = winreg.EnumValue(netkey, 1)
            macaddr = var2addr(mac)
            netname = str(ssid)
            print('[+] Net name: ' + netname + '\n macaddr: ' + macaddr)
            # 关闭句柄
            winreg.CloseKey(netkey)
        except:
            break

def main():
    print_nets()

if __name__ == '__main__':
    main()
