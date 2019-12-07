# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return "hello python!!!"

@app.route('/demo1')
def demo1():
    my_list=[1,2,3,4,5,6,7,8]
    my_int=100
    my_str1="百度一下，你就知道"
    my_str="<script>for (var i=0;i<10;i++){alert('哈哈')}</script>"
    my_dict={
        "name":"wangcan",
        "age":18

    }
    my_dict_list = [
        {
            "good_name": "大白菜",
            "price": 18,
        },
        {
            "good_name": "白",
            "price": 10,
        }
    ]
    return render_template('day05_template.html',
                           my_list=my_list,
                           my_int=my_int,
                           my_str=my_str,
                           my_dict=my_dict,
                           my_str1=my_str1,
                           my_dict_list=my_dict_list,
                           )

# 方式一：装饰器的方式
# @app.template_filter('lireverse')
def do_lireverse(li):
    # 将传入的列表转成一个新的列表，
    temp=list(li)
    # 再将新的列表进行反转
    temp.reverse()
    # li.reverse()
    # return li
    return temp

# 方式二：直接添加
app.add_template_filter(do_lireverse,"lireverse")

if __name__ == '__main__':
    app.run(debug=True)
