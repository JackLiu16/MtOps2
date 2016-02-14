#-*- coding:utf8 -*-
"""MtOps2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from djauth_ext.forms import UserPwdUpdateForm


urlpatterns = [
    url( # grappelli URLS，在 url(r'^admin/', include(admin.site.urls)) 之前引用
        r'^grappelli/', include('grappelli.urls')
       ),
    url( # admin URL
        r'^admin/', include(admin.site.urls)
       ),
    url( # 包含 asset URL
        r'^asset/', include('asset.urls')
       ),
    url( # 包含 code_update URL
        r'^code-update/', include('code_update.urls')
       ),
    url(
        r'^dbop/', include('dbop.urls')
       ),
]

urlpatterns += [ # 使用 Django auth 提供的登录、注销视图
    url( # 平台登录
        r'^auth/user/login/$', auth_views.login, {'template_name': 'login_page.html'}, name='user-login'
       ),
    url( # 用户注销
        r'^auth/user/logout/$', auth_views.logout_then_login, name='user-logout'
       ),
    url( # 用户密码修改
        r'^auth/user/pwd-change/$', auth_views.password_change, {'template_name': 'djauth_ext/pwd_update_page.html', 'password_change_form': UserPwdUpdateForm,
        'post_change_redirect': auth_views.logout_then_login},
        name='djauth_ext-userpwd-change'
       ),
    url( # 包含 djauth_ext URL
        r'auth/', include('djauth_ext.urls')
       ),
]
