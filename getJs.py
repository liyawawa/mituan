#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/26 0026 11:11
# @Author  : liya
# @Site    : 
# @File    : getJs.py

##获取js
from lxml import etree
import requests

response = requests.get('http://www.mibangfantuan.com/index.php?m=content&c=index&a=lists&catid=9')

html = etree.HTML(response.text)

result = html.xpath('//script/@src')

for jName in result:
	print jName


