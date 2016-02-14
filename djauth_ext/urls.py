# -*- coding:utf8 -*-
from django.conf.urls import url

from views import userinfo_detail_view


urlpatterns = [
    url(
        r'user/info-detail/$', userinfo_detail_view, name='djauth_ext-userinfo-detail'
       ),
]
