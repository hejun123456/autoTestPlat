from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate

# Create your views here.


def login(request):
    # 判断method
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/index/')
            return response
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误！'})

    # 如果请求方法不是post，直接返回登录页面
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')
