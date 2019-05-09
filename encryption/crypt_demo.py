#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019-5-9 9:56 
# @Author : Mark 
# @Site :  
# @File : crypt_demo.py 
# @Software: PyCharm Community Edition
# 加密工具，加密形式为crypt模块中就一个函数，crypt(str,salt) --> string
# salt为加盐值
import crypt

def test_password(crypt_password):
    salt = crypt_password[0:2]
    with open('password_file.txt') as f:
        for word in f.readlines():
            crypt_word = crypt.crypt(word.strip('\n'), salt)
            if crypt_word == crypt_password:
                print('[+] found password ' + word)
                return
        print('[-] password not found.')
        return
def _main():
    with open('download_password.txt') as f:
        for line in f.readlines():
            if ':' in line:
                user = line.split(':')[0]
                crypt_password = line.split(':')[1].strip(' ')
                print('[*] Cracking passwrod for: ' + user)
                test_password(crypt_password)

if __name__ == '__main__':
    _main()
