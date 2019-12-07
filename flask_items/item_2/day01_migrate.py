# !/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# MigrateCommand：迁移的命令
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
app.secret_key = "asdfdf"

# 配置数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123@127.0.0.1:3306/migratetest"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/migratetest"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# 使用迁移类将应用和数据库连接对象保存起来
Migrate(app, db)
# 创建终端命令的对象
manager = Manager(app)
# 将数据库的迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64), unique=True)
    # 标题
    title = db.Column(db.String(64))
    us = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()