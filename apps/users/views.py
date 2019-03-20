from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.backends import ModelBackend

from users.forms import LoginForm, RegisterForm
from utils.eamil_send import send_register_email
from .models import UserProfile
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import make_password


# 此方法需要在setting中设置
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 这样写 邮箱，用户名都能登录成功
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # 只能拿到一个
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# Create your views here.

def user_login(request):
    print(request.method)
    if request.method == "POST":
        user_name = request.POST.get("username")
        user_pwd = request.POST.get("password")
        print("user_name:  ", user_name)
        print("user_pwd:  ", user_pwd)
        form = LoginForm(request)
        if form.is_valid():
            user = auth.authenticate(username=user_name, password=user_pwd)
            if user is not None:
                auth.login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {"msg": "用户名或者密码错误"})
        else:
            return render(request, 'login.html', {"msg": "用户名或者密码输入格式不对"})
    elif request.method == "GET":
        user_name = "admin"
        pass_word = "123"

        return render(request, 'login.html', {})


class LoginView(View):
    # django会根据请求类型来访问下面的方法
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        user_name = request.POST.get("username", "admin")
        user_pwd = request.POST.get("password", "admin")
        print("user_name:  ", user_name)
        print("user_pwd:  ", user_pwd)
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=user_name, password=user_pwd)
            if user is not None:
                auth.login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {"msg": "用户名或者密码错误"})
        else:
            return render(request, 'login.html', {"login_form": form})


class Registeriew(View):
    def get(self, request):
        register_from = RegisterForm()
        return render(request, "register.html", {"register_from": register_from})

    def post(self, request):
        register_from = RegisterForm(request.POST)
        if register_from.is_valid():
            user_name = request.POST.get("email", "admin")
            user_pwd = request.POST.get("password", "admin")
            print(user_name)
            print(user_pwd)
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(user_pwd)
            user_profile.save()
            send_register_email(user_name, "register")
            return render(request, "register.html", {"register_from": register_from})
        return render(request, "register.html", {"register_from": register_from})
