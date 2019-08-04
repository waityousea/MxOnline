# _*_ coding: utf-8 _*_ 

__author__ = 'astra'
__date__ = '2019/8/4 16:23'
from django import forms


class LoginForm(forms.Form):

    #html中定义的名字必须和方法中的名字一致，否则会出错
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

