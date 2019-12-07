# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, make_response, request

app = Flask(__name__)


#,1，设置cookie
@app.route('/cookie')
def set_cookie():
    resp=make_response('this is to set cookie')
    resp.set_cookie('user_id','I love you !',max_age=3600)
    resp.set_cookie('user_name', 'wangcan', max_age=3600)
    return resp

# 2，获取cookie
@app.route('/')
def index():
    user_id=request.cookies.get('user_id')
    user_name=request.cookies.get('user_name')
    # return "hello python!!!"
    return '%s---%s'%(user_id,user_name)

#,3，删除cookie
@app.route('/logout')
def logout():
    resp=make_response("success")
    resp.delete_cookie('user_id')
    resp.delete_cookie('user_name')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
