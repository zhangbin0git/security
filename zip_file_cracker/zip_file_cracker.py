#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-04-26 1:01
# @Author  : Zhang Bin
# @Site    : home
# @File    : zip_file_cracker.py
# @Software: PyCharm

import zipfile
import optparse
from threading import Thread

def extract_file(file, password):
    """测试密码是否能开启文件"""
    try:
        file.extractall(pwd=password)
        print '[+] Found password: ' + password + '\n'
    except:
        pass

def main():
    """主程序"""
    # 规定参数
    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string',
                      help='specify dictionaty file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    # 载入压缩文件
    z_file = zipfile.ZipFile(zname)
    # 打开密码文件，对压缩文件暴力破解密码
    with open(dname, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            t = Thread(target=extract_file, args=(z_file, password))
            t.start()


if __name__ == '__main__':
    main()
