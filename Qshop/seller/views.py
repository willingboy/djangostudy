import functools

from flask import Blueprint
from flask import redirect, render_template
from flask import request, session

from seller.models import *

seller_bl = Blueprint("seller", __name__, static_url_path="/static/", static_folder="../static",
                      template_folder="../templates")


def islogin(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        cookie_username = request.cookies.get("username")
        session_email = session["email"]
        if cookie_username and session_email:
            user = User.query.filter_by(email=session_email, user_type=1).first()
            if user and cookie_username == user.username:
                return func(user, *args, **kwargs)
        return redirect("/")

    return inner


@seller_bl.route("/")
@islogin
def index(user):
    page_title = "天天生鲜 - 商家主页"
    return render_template("seller/index.html", **locals())


@seller_bl.route("/goodsapi/", methods=["GET", "POST", "PUT", "DELETE"])
@islogin
def goodsapi(user):
    result = {
        'code': 1000,
        'msg': '',
        'method': '',
        'data': []
    }
    if request.method == "POST":
        data = request.form.to_dict()
        goods = Goods()
        goods.goods_store = user.id
        # goods.goods_store = 1
        k_list = dir(goods)
        for k in k_list:
            if k.startswith("goods_"):
                if data.get(k):
                    if k == "goods_status":
                        setattr(goods, k, bool(data[k]))
                    else:
                        setattr(goods, k, data[k])
                elif getattr(goods, k) is None:
                    result['code'] = 404
                    result['msg'] = "添加商品错误"
                    return result
        db.session.add(goods)
        db.session.commit()
        result['code'] = 200
        result['msg'] = '添加商品成功'
        result['data'] = [{
            'id': goods.id,
            'goods_number': goods.goods_number,
            'goods_name': goods.goods_name,
            'goods_price': goods.goods_price,
            'goods_count': goods.goods_count,
            'goods_location': goods.goods_location,
            'goods_safe_date': goods.goods_safe_date,
            'goods_pro_time': goods.goods_pro_time,
            'goods_status': goods.goods_status,
            'goods_picture': goods.goods_picture,
            'goods_description': goods.goods_description,
            'goods_type': goods.goods_type
        }, ]
        return result
    elif request.method == "PUT":
        data = request.form.to_dict()
        goods = Goods.query.filter_by(id=data['id'], good_store=user.id).first()
        if goods:
            k_list = dir(goods)
            for k in k_list:
                if k.startswith("goods_") and data.has_key(k):
                    setattr(goods, k, data[k])
            db.session.commit()
            result['code'] = 200
            result['msg'] = '商品修改成功'
            result['data'] = [{
                'id': goods.id,
                'goods_number': goods.goods_number,
                'goods_name': goods.goods_name,
                'goods_price': goods.goods_price,
                'goods_count': goods.goods_count,
                'goods_location': goods.goods_location,
                'goods_safe_date': goods.goods_safe_date,
                'goods_pro_time': goods.goods_pro_time,
                'goods_status': goods.goods_status,
                'goods_picture': goods.goods_picture,
                'goods_description': goods.goods_description,
                'goods_type': goods.goods_type
            }, ]
            return result
        result['code'] = 404
        result['msg'] = "商品修改错误"
        return result
    elif request.method == "DELETE":
        id = request.form.get("id")
        goods = Goods.query.get(id)
        if id and goods:
            db.session.delete(goods)
            db.session.commit()
        result['code'] = 200
        result['msg'] = '商品删除成功'
        return result
    data = request.args.to_dict()
    if data:
        goods_list = Goods.query.all()
    else:
        goods_list = Goods.query.filter_by(goods_store=user.id).all()
        for goods in goods_list:
            data = {
                'id': goods.id,
                'goods_number': goods.goods_number,
                'goods_name': goods.goods_name,
                'goods_price': goods.goods_price,
                'goods_count': goods.goods_count,
                'goods_location': goods.goods_location,
                'goods_safe_date': goods.goods_safe_date,
                'goods_pro_time': goods.goods_pro_time,
                'goods_status': goods.goods_status,
                'goods_picture': goods.goods_picture,
                'goods_description': goods.goods_description,
                'goods_type': goods.goods_type
            }
            result['data'].append(data)
        result['code'] = 200
        result['msg'] = '商品查询成功'
        return result


@seller_bl.route("/goods/")
@islogin
def add_goods(user):
 pass