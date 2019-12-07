# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, session

app = Flask(__name__)

# 设置cookie
app.config['SECRET_KEY']="YOU KANG MI!"

# 获取session
@app.route('/')
def index():
    user_id=session.get('user_id','')
    user_nane=session.get('user_name','')
    return '%s----%s'%(user_id,user_nane)
    # return "hello python!!!"

#1，设置session
@app.route('/login')
def login():
    session['user_id']="I love you !"
    session['user_name']="wangcan"
    return "success"

# 删除session
@app.route('/logout')
def logout():
    session.pop('user_id')
    session.pop('user_name')
    return "success"

if __name__ == '__main__':
    app.run(debug=True)
