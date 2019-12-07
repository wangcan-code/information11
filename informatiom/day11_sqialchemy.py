from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1.配置数据库连接地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:weiwei@127.0.0.1:3306/test'
# 2.是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 3.控制台打印sql语句
app.config['SQLALCHEMY_ECHO'] = True

# 4.初始化 SQLALCHEMY 对象
db = SQLAlchemy(app)


# 角色 一的一方
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # backref 在这行代码的作用是：给前面的 User 添加一个属性，名字叫 backref 的值
    # 以便可以直接通过 user.role 方法取到一的一方的数据
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role {} {}'.format(self.id, self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 添加外键记录一的一方的主键 id，为了能够直接查询出一的一方的数据
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return 'User{} {}', format(self.id, self.name)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add_all([ro1, ro2])
    db.session.commit()

    user1 = User(name='laowang', role_id=ro1.id)
    user2 = User(name='laoli', role_id=ro1.id)
    user3 = User(name='laozhang', role_id=ro2.id)

    db.session.add_all([user1, user2, user3])
    db.session.commit()


    app.run(port=8888, debug=True)
