from flask import render_template, redirect, make_response
from flask import request, session

from Qshop import app
from Qshop.models import db, User


@app.route("/")
def index():
    cookie_username = request.cookies.get("username")
    session_email = session.get("email")
    if session_email:
        user = User.query.with_entities(User.username, User.user_type).filter_by(email=session_email, status=1).first()
        if cookie_username and user and cookie_username == user.username:
            if user.user_type:
                return redirect("/seller")
            return redirect("/buyer")
    return redirect("/login.html")


@app.route("/login.html", methods=["GET", "POST"])
def login():
    params = {
        "page_title": "天天生鲜 - 用户登陆"
    }
    if request.method == "POST":
        data = request.form
        username = data.get("username")
        pwd = data.get("pwd")
        if username and pwd and User.query.filter_by(username=username, password=pwd, status=1).first():
            user = User.query.filter_by(username=username, password=pwd, status=1).first()
            response = redirect("/")
            response.set_cookie(key="username", value=user.username)
            session["email"] = user.email
            return response
    response = make_response(render_template("auth/login.html", **params))
    session_email = session.get("email")
    if session_email:
        del session["email"]
    response.delete_cookie("username")
    return response


@app.route("/register.html", methods=["GET", "POST"])
def register():
    params = {
        "page_title": "天天生鲜 - 用户注册"
    }
    if request.method == "POST":
        data = request.form
        user_name = data.get("user_name")
        pwd = data.get("pwd")
        email = data.get("email")
        if user_name and User.query.filter_by(username=user_name).first():
            params.update({
                "user_name_error": 'style="display: inline;"'
            })
        elif email and User.query.filter_by(email=email).first():
            params.update({
                "email_error": 'style="display: inline;"'
            })
        else:
            user = User()
            user.username = user_name
            user.password = pwd
            user.email = email
            db.session.add(user)
            db.session.commit()
            return redirect("/login.html")
    return render_template("auth/register.html", **params)
