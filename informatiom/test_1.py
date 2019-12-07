# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import  Flask
app=Flask(__name__)
app.config.from_pyfile('config.ini')
@app.route('/')
def index():
    return "你好漂亮"
if __name__ == '__main__':
    app.run(port=8080,debug=True)