# -*- coding:utf8 -*-
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required

from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from models import ProjectModel, IdcModel, CabinetModel, HardwareModel, HostModel

from forms import (ProjectCreateForm, IdcCreateForm, CabinetCreateForm, HardwareCreateForm,
                   HostCreateForm)


class ProjectCreateView(CreateView):
    """
    创建软件项目
    """
    model = ProjectModel
    form_class = ProjectCreateForm
    template_name = 'asset/project_create_page.html'
    success_url = reverse_lazy('asset-project-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.add_projectmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProjectCreateView, self).dispatch(*args, **kwargs)


class ProjectUpdateView(UpdateView):
    """
    更新软件项目
    """
    model = ProjectModel
    pk_url_kwarg = 'project_id'
    form_class = ProjectCreateForm
    template_name = 'asset/project_update_page.html'
    success_url = reverse_lazy('asset-project-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.change_projectmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)


class GetDeleteMixin(object):
    """
    Django 提供的 DeleteView 通用试图默认 get() 方法用做渲染删除成功页面，
    由于项目使用 GET 方式删除，所以这里重写 get() 方法调用 delete()。
    """
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class ProjectDeleteView(GetDeleteMixin, DeleteView):
    """
    删除软件项目
    """
    model = ProjectModel
    pk_url_kwarg = 'project_id'
    success_url = reverse_lazy('asset-project-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.delete_projectmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)


class ProjectListView(ListView):
    """
    软件项目列表
    """
    model = ProjectModel
    ordering = '-put_date'
    template_name = 'asset/project_list_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectListView, self).dispatch(*args, **kwargs)

#class ProjectDetailView(DetailView):
#    """
#    项目详情
#    """
#    model = ProjectModel
#    pk_url_kwarg = 'project_id'
#    template_name = 'asset/project_detail_page.html'

#    @method_decorator(login_required)
#    def dispatch(self, *args, **kwargs):
#        return super(ProjectDetailView, self).dispatch(*args, **kwargs)

class IdcCreateView(CreateView):
    """
    创建机房
    """
    model = IdcModel
    form_class = IdcCreateForm
    template_name = 'asset/idc_create_page.html'
    success_url = reverse_lazy('asset-idc-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.add_idcmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(IdcCreateView, self).dispatch(*args, **kwargs)


class IdcUpdateView(UpdateView):
    """
    更新软件项目
    """
    model = IdcModel
    pk_url_kwarg = 'idc_id'
    form_class = IdcCreateForm
    template_name = 'asset/idc_update_page.html'
    success_url = reverse_lazy('asset-idc-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.change_idcmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(IdcUpdateView, self).dispatch(*args, **kwargs)


class IdcDeleteView(GetDeleteMixin, DeleteView):
    """
    删除软件项目
    """
    model = IdcModel
    pk_url_kwarg = 'idc_id'
    success_url = reverse_lazy('asset-idc-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.delete_idcmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(IdcDeleteView, self).dispatch(*args, **kwargs)


class IdcListView(ListView):
    """
    机房列表
    """
    model = IdcModel
    ordering = '-put_date'
    template_name = 'asset/idc_list_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IdcListView, self).dispatch(*args, **kwargs)


class CabinetCreateView(CreateView):
    """
    创建机房
    """
    model = CabinetModel
    form_class = CabinetCreateForm
    template_name = 'asset/cabinet_create_page.html'
    success_url = reverse_lazy('asset-cabinet-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.add_cabinetmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(CabinetCreateView, self).dispatch(*args, **kwargs)


class CabinetUpdateView(UpdateView):
    """
    更新软件项目
    """
    model = CabinetModel
    pk_url_kwarg = 'cabinet_id'
    form_class = CabinetCreateForm
    template_name = 'asset/cabinet_update_page.html'
    success_url = reverse_lazy('asset-cabinet-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.change_cabinetmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(CabinetUpdateView, self).dispatch(*args, **kwargs)


class CabinetDeleteView(GetDeleteMixin, DeleteView):
    """
    删除软件项目
    """
    model = CabinetModel
    pk_url_kwarg = 'cabinet_id'
    success_url = reverse_lazy('asset-cabinet-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.delete_cabinetmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(CabinetDeleteView, self).dispatch(*args, **kwargs)


class CabinetListView(ListView):
    """
    软件项目列表
    """
    model = CabinetModel
    ordering = '-put_date'
    template_name = 'asset/cabinet_list_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CabinetListView, self).dispatch(*args, **kwargs)


class HardwareCreateView(CreateView):
    """
    创建主机硬件
    """
    model = HardwareModel
    form_class = HardwareCreateForm
    template_name = 'asset/hardware_create_page.html'
    success_url = reverse_lazy('asset-hardware-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.add_hardwaremodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(HardwareCreateView, self).dispatch(*args, **kwargs)


class HardwareUpdateView(UpdateView):
    """
    更新主机硬件
    """
    model = HardwareModel
    pk_url_kwarg = 'hardware_id'
    form_class = HardwareCreateForm
    template_name = 'asset/hardware_update_page.html'
    success_url = reverse_lazy('asset-hardware-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.change_hardwaremodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(HardwareUpdateView, self).dispatch(*args, **kwargs)


class HardwareDeleteView(GetDeleteMixin, DeleteView):
    """
    删除主机硬件
    """
    model = HardwareModel
    pk_url_kwarg = 'hardware_id'
    success_url = reverse_lazy('asset-hardware-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.delete_hardwaremodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(HardwareDeleteView, self).dispatch(*args, **kwargs)


class HardwareListView(ListView):
    """
    主机硬件列表
    """
    model = HardwareModel
    ordering = '-put_date'
    template_name = 'asset/hardware_list_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HardwareListView, self).dispatch(*args, **kwargs)


class HostCreateView(CreateView):
    """
    创建主机信息
    """
    model = HostModel
    form_class = HostCreateForm
    template_name = 'asset/host_create_page.html'
    success_url = reverse_lazy('asset-host-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.add_hostmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(HostCreateView, self).dispatch(*args, **kwargs)


class HostUpdateView(UpdateView):
    """
    更新主机信息
    """
    pass
    model = HostModel
    pk_url_kwarg = 'host_id'
    form_class = HostCreateForm
    template_name = 'asset/host_update_page.html'
    success_url = reverse_lazy('asset-host-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.change_hostmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(HostUpdateView, self).dispatch(*args, **kwargs)


class HostDeleteView(GetDeleteMixin, DeleteView):
    """
    删除主机
    """
    model = HostModel
    pk_url_kwarg = 'host_id'
    success_url = reverse_lazy('asset-host-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('asset.delete_hostmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(HostDeleteView, self).dispatch(*args, **kwargs)


class HostDetailView(DetailView):
    """
    项目详情
    """
    model = HostModel
    pk_url_kwarg = 'host_id'
    template_name = 'asset/host_detail_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HostDetailView, self).dispatch(*args, **kwargs)


class HostListView(ListView):
    """
    主机信息列表
    """
    model = HostModel
    ordering = '-put_date'
    template_name = 'asset/host_list_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(HostListView, self).dispatch(*args, **kwargs)
