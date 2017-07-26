#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/26 0026 18:00
# @Author  : liya
# @Site    : 
# @File    : getCss.py

from lxml import html, etree
import requests

response = requests.get('http://www.mibangfantuan.com/')

html = etree.HTML(response.text)

result = html.xpath('//link[@type="text/css"]/@href')

for jName in result:
	print jName



