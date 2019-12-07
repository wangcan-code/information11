# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def index():
    return "hello python!!!"

# 请求数据post，传入照片,用postman进行请求
@app.route('/upload',methods=['POST'])
def upload():
    file=request.files.get('pic')
    file.save('./static/aaaa.png')
    return "success"

# 请求数据post，传入数据，用postman进行请求
@app.route('/data',methods=['POST'])
def data():
    data=request.data
    print(data)
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
