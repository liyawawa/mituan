#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 7/31 0031 16:51
# @Author  : liya
# @Site    : 
# @File    : hello.py

from flask import render_template

## 欢迎页
from flask import Flask
app = Flask(__name__)

@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/center/')
def center():
    return render_template('center.html')


@app.route('/lianxi/')
def lianxi():
    return render_template('lianxi.html')


@app.route('/product/')
def product():
    return render_template('product.html')


@app.route('/shaobing/')
def shaobing():
    return render_template('shaobing.html')


@app.route('/shop/')
def shop():
    return render_template('shop.html')


@app.route('/zixun/')
def zixun():
    return render_template('zixun.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
