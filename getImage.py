#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/26 0026 11:05
# @Author  : liya
# @Site    : 
# @File    : getImage.py


##获取网页图片
import re
import os
import urllib
from lxml import etree

import requests


response = requests.get('http://www.mibangfantuan.com/index.php?m=content&c=index&a=lists&catid=9')

html = etree.HTML(response.text)

urllist = html.xpath('//img/@src')

for jName in urllist:
	print jName


if not urllist:
    print 'not found...'
else:
    # 下载图片,保存在当前目录的image文件夹下
    filepath = os.getcwd() + '\image'
    if os.path.exists(filepath) is False:
        os.mkdir(filepath)
    x = 1
    print u'爬虫准备就绪...'
    for imgurl in urllist:

        p = re.compile(r'/')
        imglist = p.split(imgurl)

        print len(imglist)
        if len(imglist) == 1:
            temp = filepath + '\%s' % imglist[0]
        else:
            temp = filepath + '\%s' % imglist[len(imglist) - 1]

        print u'正在下载第%s张图片' % x
        print imgurl +'-----------------'+ temp
        urllib.urlretrieve(imgurl, temp)
        x += 1
    print u'图片下载完毕，保存路径为' + filepath
