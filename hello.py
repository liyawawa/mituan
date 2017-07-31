#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/31 0031 16:51
# @Author  : liya
# @Site    : 
# @File    : hello.py


## 欢迎页
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
