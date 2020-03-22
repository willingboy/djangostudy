from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.

def isbuyerlogin(func):
    def islogin(request, *args, **kwargs):
        cookie_email = request.COOKIES.get('email')
        session_email = request.session.get('email')
        if cookie_email and session_email and LoginUser.objects.filter(email=session_email).exists():
            user = LoginUser.objects.filter(email=session_email).first()
            response = func(request, user, *args, **kwargs)
            return response
        return HttpResponseRedirect('/login.html')

    return islogin


@isbuyerlogin
def index(request, user):
    params = {
        'page_title': '天天生鲜 - 首页',
        'user': user,
        'goods_type': GoodsType.objects.all()
    }

    return render(request=request, template_name='index.html', context=params)


@isbuyerlogin
def listpage(request, user):
    if request.method == "GET":
        type_description = request.GET.get("type")
        if type_description:
            params = {
                'page_titile': '天天生鲜 - 商品列表',
                'user': user,
                'this_type': GoodsType.objects.filter(type_description=type_description).first(),
                'goods_type': GoodsType.objects.all(),
            }
            return render(request, 'list.html', params)
    return HttpResponseRedirect('/buyer/index.html')


@isbuyerlogin
def detail(request, user):
    params = {
        'page_title': '天天生鲜 - 商品详情',
        'user': user
    }
    if request.method == "POST":
        pass
    elif request.method == "GET":
        id = request.GET.get('id')
        goods = Goods.objects.filter(id=id).first()
        if goods:
            params.update({
                'goods': goods,
                'goods_type': GoodsType.objects.all()
            })
            if LookHistory.objects.filter(user=user, goods_id=id).exists():
                LookHistory.objects.filter(user=user, goods_id=id).delete()
            if LookHistory.objects.filter(user=user).count() > 4:
                LookHistory.objects.filter(user=user).first().delete()
            LookHistory.objects.create(user=user, goods_id=id)
            return render(request, 'detail.html', params)
    return HttpResponseRedirect('/index.html')


@isbuyerlogin
def cart(request, user):
    from django.http import JsonResponse, QueryDict
    from django.db.models import F
    import json, time
    result = {
        'code': 1000,
        'msg': '成功',
        'data': ''
    }
    if request.method == "POST":
        data = json.loads(request.POST.get("data"))
        print(data)
        if data:
            payorder = PayOrder()
            user_site = UserSite.objects.filter(user=user, status=1).first()
            if user_site:
                payorder.order_address = f"{user_site.sitearea} ({user_site.username} 收) {user_site.phone}"
            payorder.order_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            payorder.order_status = 1
            payorder.order_total = None
            payorder.order_user = user
            payorder.save()
            payorder.order_number = payorder.id + int(56000000)
            payorder.save()
            for i in data:
                if i['id'] and i['num'] and Goods.objects.filter(id=i['id']).exists():
                    orderinfo = OrderInfo()
                    orderinfo.order = payorder
                    orderinfo.goods = Goods.objects.filter(id=i['id']).first()
                    orderinfo.goods_count = i['num']
                    orderinfo.goods_price = Goods.objects.filter(id=i['id']).first().goods_price
                    orderinfo.goods_total_price = float(i['num']) * Goods.objects.filter(id=i['id']).first().goods_price
                    orderinfo.save()
                    cart = Cart.objects.filter(cart_user=user, goods_id=i['id'])
                    if cart:
                        cart.delete()
            result["url"] = "/buyer/place_order.html"
            return JsonResponse(data=result, json_dumps_params={'ensure_ascii': False})
    elif request.method == "DELETE":
        delete = QueryDict(request.body)
        id = delete.get('id')
        if id and Cart.objects.filter(goods_id=id, cart_user=user).exists():
            Cart.objects.filter(goods_id=id, cart_user=user).delete()
            result['msg'] = '删除成功'
            result['data'] = Goods.objects.filter(id=id).first().goods_name
            return JsonResponse(data=result, json_dumps_params={'ensure_ascii': False})
    elif request.method == "PUT":
        put = QueryDict(request.body)
        id = put.get('id')
        num = put.get('num')
        if id and Goods.objects.filter(id=id).exists():
            if num is None:
                if Cart.objects.filter(goods_id=id, cart_user=user).exists():
                    Cart.objects.filter(goods_id=id, cart_user=user).update(goods_number=F('goods_number') + 1)
                else:
                    Cart.objects.create(goods_id=id, goods_number=1, cart_user=user)
                result['msg'] = "添加成功"

            elif Cart.objects.filter(goods_id=id, cart_user=user).exists():
                if int(num) == 0:
                    Cart.objects.filter(goods_id=id, cart_user=user).delete()
                    result['msg'] = '删除成功'
                else:
                    Cart.objects.filter(goods_id=id, cart_user=user).update(goods_number=int(num))
                    result['msg'] = '修改成功'
            else:
                Cart.objects.create(goods_id=id, goods_number=int(num), cart_user=user)
                result['msg'] = "添加成功"
            result['data'] = Cart.objects.filter(cart_user=user, goods_id=id).first().goods_number
            response = JsonResponse(data=result, json_dumps_params={'ensure_ascii': False})
            response['Access-Control-Allow-Origin'] = '*'
            return response
    elif request.method == "GET":
        params = {
            'page_title': '天天生鲜 - 购物车',
            'user': user
        }
        return render(request, 'cart.html', params)

    result['code'] = 4000
    result['msg'] = '失败'
    return JsonResponse(data=result, json_dumps_params={'ensure_ascii': False})


@isbuyerlogin
def place_order(request, user: LoginUser):
    from buyer import other
    import json
    if request.method == "POST":
        data = request.POST.get("data")
        data = json.loads(data)[0]
        order = other.Alipay()
        url = order.orders(data, user)
        print(url)
        return HttpResponse(url)
        # return HttpResponseRedirect("/index.html")
    upay_order = user.payorder_set.filter(order_status=1).last()
    user_site = UserSite.objects.filter(user=user, status=1).first()
    upay_order.order_address = f"{user_site.sitearea} ({user_site.username} 收) {user_site.phone}"
    upay_order.save()
    params = {
        "page_title": "天天生鲜 - 结算",
        "user": user,
        "upay_order": upay_order
    }
    return render(request, 'place_order.html', params)


@isbuyerlogin
def user_center_site(request, user: LoginUser):
    params = {
        'page_title': '天天生鲜 - 地址管理',
        'user': user
    }
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        sitearea = data.get("sitearea")
        code = data.get("code")
        phone = data.get("phone")
        if username and sitearea and code and phone:
            if UserSite.objects.filter(user=user, status__in=[1, 2]).exists():
                UserSite.objects.filter(user=user, status__in=[1, 2]).update(status=2)
            UserSite.objects.create(user=user, username=username, sitearea=sitearea, code=code, phone=phone)
    elif request.method == "GET":
        id = request.GET.get("id")
        if id and UserSite.objects.filter(user=user, id=id).exists():
            UserSite.objects.filter(user=user, status=1).update(status=2)
            UserSite.objects.filter(user=user, id=id).update(status=1)
    cur_usersite = UserSite.objects.filter(user=user, status=1).first()
    his_usersite = UserSite.objects.filter(user=user, status=2).all()
    params.update(
        {
            'cur_usersite': cur_usersite,
            'his_usersite': his_usersite
        }
    )
    return render(request, "user_center_site.html", params)


@isbuyerlogin
def user_center_info(request, user: LoginUser):
    params = {
        'page_title': '天天生鲜 - 用户信息',
        'user': user,
        'cur_usersite': user.usersite_set.filter(status=1).first(),
        'look_history': user.lookhistory_set.order_by("-datatime").all()
    }
    return render(request, "user_center_info.html", params)


@isbuyerlogin
def user_center_order(request, user: LoginUser):
    params = {
        'page_title': '天天生鲜 - 订单中心',
        'user': user,
        'order': user.payorder_set.all()
    }
    return render(request=request, template_name="user_center_order.html", context=params)


def alipay(request):
    print("==================================")
    print("method:\n", request.method)
    print("headers:\n", request.headers)
    print("body:\n", request.body)
    print("scheme:\n", request.scheme)
    print('remote_addr',request.META.get("REMOTE_ADDR"))
    return HttpResponse("付款成功")
