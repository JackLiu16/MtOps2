#-*- coding:utf8 -*-
from django.conf.urls import url

from views import (ProjectUpdateView, ProjectListView, TaskCreateView, TaskListView,
                   TaskUpdateView, TaskDeleteView, TaskRunLogView)


urlpatterns = [
    url( # 软件项目注册
        r'project/(?P<project_id>\d+)/update/$', ProjectUpdateView.as_view(),
        name='code-project-update',
       ),
    url( # 软件项目列表
        r'project/list/$', ProjectListView.as_view(),
        name='code-project-list',
       ),
    url( # 上线任务创建
        r'task/create/$', TaskCreateView.as_view(),
        name='code-task-create',
       ),
    url( # 上线任务更新
        r'task/(?P<task_id>\d+)/update/$', TaskUpdateView.as_view(),
        name='code-task-update',
       ),
    url( # 上线任务删除
        r'task/(?P<task_id>\d+)/delete/$', TaskDeleteView.as_view(),
        name='code-task-delete',
       ),
    url( # 查看后台任务执行输出
        r'task/(?P<task_id>\d+)/runlog/$', TaskRunLogView.as_view(),
        name='code-task-runlog',
       ),
    url( # 上线任务列表
        r'task/list/$', TaskListView.as_view(),
        name='code-task-list',
       ),
]
