# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 创建manager与app关联
manager=Manager(app)
# 可以通过命令行在运行时指定运行的端口
@app.route('/')
def index():
    return "hello python!!!"

if __name__ == '__main__':
    # app.run(debug=True)
    # 使用manager进行运行
    manager.run()