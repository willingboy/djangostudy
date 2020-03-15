from flask import render_template

from demo.models import *


def index():
    return render_template("index.html")


def dbtest():
    roles = Role.query.all()
    for i in roles:
        print(i.r_name)
    return "测试数据库"
