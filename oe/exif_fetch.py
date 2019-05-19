#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-13 上午12:43
# @Author  : Zhangbin
# @Site    : 
# @File    : exif_fetch.py
# @Software: PyCharm
# 在指定的网站下载图片并分析

import os
import requests
import optparse
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS
import piexif

def find_images(url):
    print('[+] Finding images on ' + url)
    r = requests.get(url)
    url_content = r.content
    soup = BeautifulSoup(url_content, "html5lib")
    img_tags = soup.findAll('img')
    return img_tags

def download_image(imgtag):
    try:
        print('[+] Downloading image...')
        img_src = imgtag['src']
        imgcontent = requests.get('https:' + img_src)
        imgfilename = os.path.basename(img_src)
        imgfile = open(imgfilename, 'wb')
        imgfile.write(imgcontent.content)
        imgfile.close()
        return imgfilename
    except:
        return ''

def test_for_exif(img_file_name):
    # 提取图片的元数据
    exif_data = {}
    img_file = Image.open(img_file_name)
    info = img_file._getexif()
    if info:
        for (tag, value) in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value
        exif_gps = exif_data['GPSInfo']
        print(str(exif_data['GPSInfo'][0], 'utf-8'))
        if exif_gps:
            print('[*] ' + img_file_name + 'contains GPS Metadata')

    # exif_dict = piexif.load(img_file_name)
    # print(exif_dict)
    # for ifd in ("0th", "Exif", "GPS", "1st"):
    #     for tag in exif_dict[ifd]:
    #         print(piexif.TAGS[ifd][tag]["name"], exif_dict[ifd][tag])
# m = find_images('https://www.baidu.com')
# f = download_image(m[0])
test_for_exif('MOX_4550--.JPG')

