# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo

app = Flask(__name__)
# 关闭csrf
app.config['WTF_CSRF_ENABLED']=False
app.secret_key="abcdefg"
# 自定义注册表单
class RegisterForm(FlaskForm):
    username=StringField('用户名:',validators=[InputRequired("亲! 输入用户名")],render_kw={'placeholder':"亲! 输入用户名"})
    password=PasswordField('密码:',validators=[InputRequired("亲! 输入密码")],render_kw={"placeholder":"亲! 输入密码"})
    password2=PasswordField('确认密码:',validators=[InputRequired("亲! 输入确认密码"),EqualTo('password',"两次密码一致")],render_kw={"placeholder":"亲! 输入确认密码"})
    submit=SubmitField('注册')


@app.route('/')
def index():
    return "hello python!!!"

# 使用 Flask-WTF 实现表单
@app.route('/register_wtf',methods=['GET','POST'])
def register_wtf():
    my_srt="web表单"
    register_form=RegisterForm()
    # 使用wtf表单帮我们做验证
    if register_form.validate_on_submit():
        #     执行注册逻辑
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        # 假装做注册操作
        print(username, password, password2)
        return "success"
    else:
        if request.method=="POST":
            flash("参数错误")

    return render_template('day10_wtf.html',my_srt=my_srt,form=register_form)


@app.route('/demo',methods=["GET","POST"])
def demo():
    my_srt='web表单'
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一致")
        else:
            # 假装做注册操作
            print(username, password, password2)
            return "success"
    return render_template('day10_wtf.html',my_srt=my_srt)

if __name__ == '__main__':
    app.run(debug=True)
