# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
app=Flask(__name__)
# app.config.from_pyfile('config.ini')
# app.config.from_envvar('FLASKCONFIG')

@app.route('/')
def index():
    return 'hello python'

if __name__ == '__main__':
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000, debug = True)
