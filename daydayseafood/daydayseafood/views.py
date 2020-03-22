from django.shortcuts import render
from django.http import HttpResponseRedirect
from seller.models import LoginUser


def index(request):
    session_email = request.session.get('email')
    cookie_email = request.COOKIES.get('email')
    if cookie_email and session_email and cookie_email == session_email:
        user = LoginUser.objects.filter(email=session_email).first()
        if user:
            if user.user_type == 0:
                return HttpResponseRedirect('/seller/index.html')
            elif user.user_type == 1:
                return HttpResponseRedirect('/buyer/index.html')
    return HttpResponseRedirect('/login.html')


def register(request):
    params = {
        'page_title': "天天生鲜 - 用户注册"
    }
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        if user_name and pwd and email:
            if LoginUser.objects.filter(username=user_name).exists():
                params.update({
                    'user_name_error': 'style="display: inline;"'
                })
            elif LoginUser.objects.filter(email=email).exists():
                params.update({
                    'email_error': 'style="display: inline;"'
                })
            else:
                user = LoginUser()
                user.username = user_name
                user.password = pwd
                user.email = email
                try:
                    user.save()
                except Exception as e:
                    print(e)
                else:
                    return HttpResponseRedirect('/login.html')
    return render(request=request, template_name="page/register.html", context=params)


def login(request):
    params = {
        'page_title': '天天生鲜 - 用户登陆'
    }
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username and pwd:
            user = LoginUser.objects.filter(username=username, password=pwd).first()
            if user:
                response = HttpResponseRedirect("/index.html")
                response.set_cookie('email', user.email)
                request.session['email'] = user.email
                return response
    response = render(request, 'page/login.html', params)
    flag = request.session.get("email")
    if flag:
        request.session.flush()
        request.session.delete()
        response.delete_cookie('email')
    return response
