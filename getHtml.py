#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/26 0026 11:31
# @Author  : liya
# @Site    : 
# @File    : getHtml.py

import os

import requests

response = requests.get('http://www.jbshaobing.com/')

text = response.text
print response.text

print os.getcwd()

path = os.getcwd()+"\html\shaobing.html"

f = open(path,'w')
f.write(text.encode('utf-8'))
f.close()