# -*- coding:utf8 -*-
from django.conf.urls import url

from views import (ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectListView,
                   IdcCreateView, IdcUpdateView, IdcDeleteView, IdcListView, CabinetCreateView,
                   CabinetUpdateView, CabinetDeleteView, CabinetListView, HardwareCreateView,
                   HardwareUpdateView, HardwareDeleteView, HardwareListView, HostCreateView,
                   HostUpdateView, HostDeleteView, HostDetailView, HostListView,
                   )

urlpatterns = [
    url( # 创建软件项目
        r'project/create/$', ProjectCreateView.as_view(),
        name='asset-project-create',
       ),
    url( # 更新软件项目
        r'project/(?P<project_id>\d+)/update/$', ProjectUpdateView.as_view(),
        name='asset-project-update',
       ),
    url( # 删除软件项目
        r'project/(?P<project_id>\d+)/delete/$', ProjectDeleteView.as_view(),
        name='asset-project-delete',
       ),
#    url( # 项目详情
#        r'project/(?P<project_id>\d+)/detail/', ProjectDetailView.as_view(),
#        name='asset-project-detail',
#       ),
    url( # 软件项目列表
        r'project/list/$', ProjectListView.as_view(),
        name='asset-project-list',
       ),
    url( # 创建机房信息
        r'idc/create/$', IdcCreateView.as_view(),
        name='asset-idc-create',
       ),
    url( # 更新机房信息
        r'idc/(?P<idc_id>\d+)/update/$', IdcUpdateView.as_view(),
        name='asset-idc-update',
       ),
    url( # 删除机房
        r'idc/(?P<idc_id>\d+)/delete/$', IdcDeleteView.as_view(),
        name='asset-idc-delete',
       ),
    url( # 机房信息列表列表
        r'idc/list/$', IdcListView.as_view(),
        name='asset-idc-list',
       ),
    url( # 创建机柜信息
        r'cabinet/create/$', CabinetCreateView.as_view(),
        name='asset-cabinet-create',
       ),
    url( # 更新机柜信息
        r'cabinet/(?P<cabinet_id>\d+)/update/$', CabinetUpdateView.as_view(),
        name='asset-cabinet-update',
       ),
    url( # 删除机柜
        r'cabinet/(?P<cabinet_id>\d+)/delete/$', CabinetDeleteView.as_view(),
        name='asset-cabinet-delete',
       ),
    url( # 机柜信息列表
        r'cabinet/list/$', CabinetListView.as_view(),
        name='asset-cabinet-list',
       ),
    url( # 创建硬件信息
        r'hardware/create/$', HardwareCreateView.as_view(),
        name='asset-hardware-create',
       ),
    url( # 更新硬件信息
        r'hardware/(?P<hardware_id>\d+)/update/$', HardwareUpdateView.as_view(),
        name='asset-hardware-update',
       ),
    url( # 删除硬件信息
        r'hardware/(?P<hardware_id>\d+)/delete/$', HardwareDeleteView.as_view(),
        name='asset-hardware-delete',
       ),
    url( # 硬件信息列表
        r'hardware/list/$', HardwareListView.as_view(),
        name='asset-hardware-list',
       ),
    url( # 创建主机信息
        r'host/create/$', HostCreateView.as_view(),
        name='asset-host-create',
       ),
    url( # 更新主机信息
        r'host/(?P<host_id>\d+)/update/$', HostUpdateView.as_view(),
        name='asset-host-update',
       ),
    url( # 删除主机信息
        r'host/(?P<host_id>\d+)/delete/$', HostDeleteView.as_view(),
        name='asset-host-delete',
       ),
    url( # 主机详细信息
        r'host/(?P<host_id>\d+)/detail/$', HostDetailView.as_view(),
        name='asset-host-detail',
       ),
    url( # 主机信息列表
        r'host/list/$', HostListView.as_view(),
        name='asset-host-list',
       ),
]
