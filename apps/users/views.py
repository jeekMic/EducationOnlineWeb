from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.backends import ModelBackend

from users.forms import LoginForm, RegisterForm, ForgetForm, ModifyForm
from utils.eamil_send import send_register_email
from .models import UserProfile, EmailVerifyRecord
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
                if user.is_active:
                    auth.login(request, user)
                    return render(request, 'index.html', {})
                else:
                    return render(request, 'login.html', {"msg": "用户未激活", "login_form": form})
            else:
                return render(request, 'login.html', {"msg": "用户名或者密码错误", "login_form": form})
        else:
            return render(request, 'login.html', {"login_form": form})


class Registeriew(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {"register_form": register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "admin")
            if UserProfile.objects.filter(email=user_name):
                # 说明邮箱已经注册过了
                return render(request, "register.html", {"msg": "邮箱已经注册"})
            user_pwd = request.POST.get("password", "admin")
            print(user_name)
            print(user_pwd)
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(user_pwd)
            user_profile.is_active = False
            user_profile.save()

            send_register_email(user_name, "register")
            return render(request, "login.html")
        return render(request, "register.html", {"register_form": register_form})


class ActiveUserView(View):
    # 用户点击了激活链接
    def get(self, request, active_code):
        print(active_code)
        print("---")
        # 查询记录是否存在
        all_recorder = EmailVerifyRecord.objects.filter(code=active_code)
        if all_recorder:
            for record in all_recorder:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                print("激活成功")
        return render(request, "login.html")


class ForgetPwView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})
    def post(self,request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email","")
            send_register_email(email, "forget")
            return render(request,"send_success.html",{})
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetUserView(View):
    # 用户点击了激活链接
    def get(self, request, reset_code):
        # 查询记录是否存在
        all_recorder = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_recorder:
            for record in all_recorder:
                email = record.email
                return render(request, "password_reset.html", {"email":email})
        else:
                return render(request, "login.html")

class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1")
            pwd2 = request.POST.get("password2")
            email = request.POST.get("email")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不一致"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()
            # 修改成功 返回登录页面
            return render(request, "login.html")
        else:
            email = request.POST.get("email")
            print(email)
            return render(request, "password_reset.html", {"email":email, "modify_form":modify_form})
