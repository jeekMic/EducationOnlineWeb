"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
import xadmin
from MxOnline.settings import MEDIA_ROOT
from django.views.generic import TemplateView
from organizations.views import OrgView
from users.views import ActiveUserView, ResetUserView, ModifyPwdView,LoginView,Registeriew,ForgetPwView
from django.views.static import serve

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    # path('login/', views.user_login, name="login"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', Registeriew.as_view(), name="register"),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)', ActiveUserView.as_view(), name="active"), # 括号提取active后面的字符串
    path('forget/', ForgetPwView.as_view(), name="forget"),
    re_path('reset/(?P<reset_code>.*)', ResetUserView.as_view(), name="reset"), # 括号提取active后面的字符串
    re_path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"), # 括号提取active后面的字符串

    # 课程机构列表
    path('org/', include("organizations.urls", namespace="org")),
    # 读取图片静态文件专用的path
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT})
]



