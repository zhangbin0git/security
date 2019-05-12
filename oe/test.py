#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 19-5-13 上午2:28
# @Author  : Zhangbin
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(fname):
    """Get embedded EXIF data from image file."""
    ret = {}
    try:
        img = Image.open(fname)
        if hasattr( img, '_getexif' ):
            exifinfo = img._getexif()
            if exifinfo != None:
                for tag, value in exifinfo.items():
                    decoded = TAGS.get(tag, tag)
                    ret[decoded] = value
    except IOError:
        print 'IOERROR ' + fname
    return ret

if __name__ == '__main__':
    fileName = 'bd_logo1.png'
    exif = get_exif_data(fileName)
    print exif