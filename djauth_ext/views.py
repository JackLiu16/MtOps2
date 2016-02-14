# -*- coding:utf8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def userinfo_detail_view(request):
    """
    用户信息详情视图
    """
    return render_to_response('djauth_ext/user_detail_page.html', context_instance=RequestContext(request))
