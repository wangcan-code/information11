# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return "hello python!!!"
@app.route("/demo1")

# 宏
def demo1():
    my_srt="宏的使用！"
    return render_template('day07_macro.html',my_srt=my_srt)

# 继承
@app.route('/demo2')
def demo2():
    my_srt="继承的使用！"
    return render_template('day08_extend.html',my_srt=my_srt)


# 抽取模版
@app.route('/news_index')
def demo3():
    return render_template('index.html')
# 抽取模版
@app.route('/news_detail')
def demo4():
    return render_template('detail.html')


# 包含
@app.route('/demo5')
def demo5():
    my_srt="包含的使用"
    return render_template('day09_include.html',my_srt=my_srt)

if __name__ == '__main__':

    # app.run(host='192.168.1.6',port='5000',debug=True)
    app.run(debug=True)