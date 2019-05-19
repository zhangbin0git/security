#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-13 上午2:28
# @Author  : Zhangbin
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from PIL import Image
#code from //www.jb51.net
img = Image.open('bd_logo1.png')
exif_data = img.getexif()
print(exif_data)
