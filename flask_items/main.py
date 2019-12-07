# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask
from order import order_blu

app = Flask(__name__)

# 3，把蓝图注册在app上
app.register_blueprint(order_blu)

@app.route('/')
def index():
    return 'hello python'
"""
以下的代码放在order.py
@app.route('/order/list')
def order_list():
    return 'orderlist'
"""


@app.route('/user/info')
def user_info():
    return 'user_info'

@app.route('/cart/list')
def cart_list():
    return 'cart_list'

if __name__ == '__main__':
    app.run(debug=True)
