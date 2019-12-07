# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# 指定路由地址
from flask import Flask
from flask import json
from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for

app=Flask(__name__)
# 指定访问路径为 demo1
@app.route('/')
def demo1():
    return '你好漂亮呀'

@app.route('/demo2')
def demo2():
    return '我好喜欢你呀'

@app.route('/user/<int:user_id>')
def demo3(user_id):
    return 'demo3 %s'%user_id

@app.route('/demo4',methods=['GET','POST'])
def demo4():
    return 'demo4%s'%request.method

@app.route('/json')
def demo5():
    json_dict={
        "name":"wangcan",
        "age":27,

    }
    return json.dumps(json_dict)

@app.route('/redirect')
def demo6():
    return redirect(url_for('demo3',user_id=8899))


@app.route('/damo7')
def demo7():
    return 'ABC'

if __name__ == '__main__':
    app.run(debug=True)