#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/26 0026 11:31
# @Author  : liya
# @Site    : 
# @File    : getHtml.py

import os

import requests

response = requests.get('http://www.mibangfantuan.com/index.php?m=content&c=index&a=lists&catid=10')

text = response.text
print response.text

print os.getcwd()

path = os.getcwd()+"\html\page.html"

f = open(path,'w')
f.write(text.encode('utf-8'))
f.close()