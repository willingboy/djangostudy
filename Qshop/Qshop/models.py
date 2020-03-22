from flask_sqlalchemy import SQLAlchemy

from Qshop import app

db = SQLAlchemy(app=app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    user_type = db.Column(db.Boolean, default=0)  # 当0时候是买家用户，当是1时候是卖家用户
    status = db.Column(db.Boolean, default=1)  # 当0的时候用户停用，当是1的时候用户可用


db.create_all()
