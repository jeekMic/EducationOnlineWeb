# _*_ coding: utf-8
from captcha.fields import CaptchaField

__author__ = 'hb'
__date__ = '2019/3/12 11:34'
from django import forms
class LoginForm(forms.Form):
    # 这里的username和password必须要和前台的form表单要一直
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
    email = forms.EmailField(required=True, error_messages={"invalid": "邮箱不正确"})
    password = forms.CharField(required=True, error_messages={"invalid": "密码输入格式不对"})

class ForgetForm(forms.Form):
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
    email = forms.EmailField(required=True, error_messages={"invalid": "邮箱不正确"})

class ModifyForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5, error_messages={"invalid": "密码输入格式不对"})
    password2 = forms.CharField(required=True, min_length=5, error_messages={"invalid": "密码输入格式不对"})
