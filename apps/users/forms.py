# _*_ coding: utf-8
__author__ = 'hb'
__date__ = '2019/3/12 11:34'
from django import forms
class LoginForm(forms.Form):
    # 这里的username和password必须要和前台的form表单要一直
    username = forms.CharField(required=True )
    password = forms.CharField(required=True, min_length=15)