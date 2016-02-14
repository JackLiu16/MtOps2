# -*-coding:utf8 -*-
from django.conf.urls import url
from views import (CTTaskCreateView, CTTaskUpdateView, CTTaskDeleteView,
                   CTTaskListView, ct_sub_task_create, )#ajax_cors_agent)

urlpatterns = [
    url( # 普通建表任务创建
        r'ct-task/create/$', CTTaskCreateView.as_view(),
        name='dbop-ct_task-create',
       ),
    url( # 更新普通建表任务
        r'ct-task/(?P<ct_task_id>\d+)/update/$', CTTaskUpdateView.as_view(),
        name='dbop-ct_task-update',
       ),
    url(
        r'ct-task/(?P<ct_task_id>\d+)/add-sql/$', ct_sub_task_create,
        name="dbop-ct_task-addsql",
       ),
    url( # 删除任务
        r'ct-task/(?P<ct_task_id>\d+)/delete/$', CTTaskDeleteView.as_view(),
        name='dbop-ct_task-delete',
       ),
    url( # 普通建表任务列表
        r'ct-task/list/$', CTTaskListView.as_view(),
        name='dbop-ct_task-list',
       ),
#    url(
#        r'cttask/(?P<ctmaintask_id>\d+)/detail/', 
#       ),
#    url( # ajax 代理视图
#        r'cttask/sql-textarex/ajaxpost-dbapi-check/$', ajax_cors_agent,
#        name='dbop-ajaxcors-agent',
#       ),
]
