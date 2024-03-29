"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from users.views import LoginView, RegisterView,ActiveUserView,ForgetPwdView,ResetUserView,ModifyPwdView

from django.urls import re_path
from django.views.static import serve
from .settings import MEDIA_ROOT

from organization.views import OrgView

import xadmin


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name = "index"),

    #path('login/', TemplateView.as_view(template_name="login.html"), name="登录页面"),
    path('login/', LoginView.as_view(), name="登录页面"),
    path('register/', RegisterView.as_view(), name="注册页面"),
    #path('users/', include('users.urls')),
    #path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    re_path('media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    url('captcha/', include('captcha.urls')),
    #用来验证邮件激活的url链接
    url('active/(?P<active_code>.*)',ActiveUserView.as_view(),name="user_active"),
    path('forget/', ForgetPwdView.as_view(), name="忘记密码"),
    url('reset/(?P<active_code>.*)', ResetUserView.as_view(),name="reset_pwd"),
    path('miodify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    #课程机构首页
    path('org_list/', OrgView.as_view(), name="org_list"),

]
