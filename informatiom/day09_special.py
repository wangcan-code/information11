# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, session, g, flash

app = Flask(__name__)
app.secret_key='abcdefghyjkmnop'
@app.route('/demo')
def index():
    return "hello python!!!"

@app.route('/demo1')
def demo1():
    session['name']="laowang"
    my_srt="模板的特有变量和函数"
    g.name="wangcan"
    flash("我是老大我怕谁")
    return render_template('day09_special.html',my_srt=my_srt)


if __name__ == '__main__':
    app.run(debug=True)
