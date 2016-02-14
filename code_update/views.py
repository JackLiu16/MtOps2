# -*- coding:utf8 -*-
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required

from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from models import ProjectProxyModel, ProjectExtModel, TaskModel

from forms import ProjectUpdateForm, TaskCreateForm, TaskUpdateForm

from guardian.shortcuts import get_objects_for_user # 第三方库，object 级别权限控制相关

from tasks import code_task


class ProjectUpdateView(UpdateView):
    """
    项目绑定上线脚本
    """
    model = ProjectExtModel
    pk_url_kwarg = 'project_id'
    form_class = ProjectUpdateForm
    template_name = 'code_update/project_update_page.html'
    success_url = reverse_lazy('code-project-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('code_update.change_projectextmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)


class ProjectListView(ListView):
    """
    项目列表
    """
    model = ProjectExtModel
    template_name = 'code_update/project_list_page.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProjectListView, self).dispatch(*args, **kwargs)


class TaskCreateView(CreateView):
    """
    创建上线任务
    """
    model = TaskModel
    form_class = TaskCreateForm
    template_name = 'code_update/task_create_page.html'
    success_url = reverse_lazy('code-task-list')

    def get_context_data(self, **kwargs):
        """
        增加额外的渲染对象
        """
        projects = get_objects_for_user(self.request.user, 'asset.view_projectproxymodel') # 获取当前登录用户所拥有可视权限的项目，用于前端 <select> 选项的渲染
        if 'projects' not in kwargs:
            kwargs['projects'] = projects
        return super(TaskCreateView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        """
        为非用户提交字段在后台自动创建相应的初始值
        """
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

    @method_decorator(login_required)
    @method_decorator(permission_required('code_update.add_taskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TaskCreateView, self).dispatch(*args, **kwargs)


class TaskUpdateView(UpdateView):
    """
    更新上线任务
    """
    model = TaskModel
    pk_url_kwarg = 'task_id'
    form_class = TaskUpdateForm
    template_name = 'code_update/task_update_page.html'
    success_url = reverse_lazy('code-task-list')

    def form_valid(self, form):
        """
        在响应 HTTP 请求之前，将后台任务与相关参数做入队操作
        """
        form.instance.yw_user = self.request.user.last_name + self.request.user.first_name # 将登录用户作为操作责任人存至相应字段

        if form.instance.schedule == '3':
            action = 'update'
        elif form.instance.schedule == '4':
            action = 'rollback'
        elif form.instance.schedule == '5':
            action = 'checkdiff'

        task_id = form.instance.id
        code_version = form.instance.code_version
        run_script = form.instance.project.projectextmodel.run_script
        mod_name = form.instance.project.project_alias

        code_task.delay(run_script, mod_name, action, code_version, task_id)

        return super(TaskUpdateView, self).form_valid(form)

    @method_decorator(login_required)
    @method_decorator(permission_required('code_update.change_taskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdateView, self).dispatch(*args, **kwargs)
    

class GetDeleteMixin(object):
    """
    Django 提供的 DeleteView 通用试图默认 get() 方法用做渲染删除成功页面，
    由于项目使用 GET 方式删除，所以这里重写 get() 方法调用 delete()。
    """
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class TaskDeleteView(GetDeleteMixin, DeleteView):
    """
    删除上线任务
    """
    model = TaskModel
    pk_url_kwarg = 'task_id'
    success_url = reverse_lazy('code-task-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('code_update.delete_taskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TaskDeleteView, self).dispatch(*args, **kwargs)


class TaskRunLogView(DetailView):
    """
    显示后台任务输出
    """
    model = TaskModel
    pk_url_kwarg = 'task_id'
    template_name = 'code_update/task_runlog_page.html'

    @method_decorator(login_required)
    @method_decorator(permission_required('code_update.add_taskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TaskRunLogView, self).dispatch(*args, **kwargs)


class TaskListView(ListView):
    """
    任务列表
    """
    model = TaskModel
    ordering = '-put_date'
    template_name = 'code_update/task_list_page.html'

    def get_queryset(self):
        """
        过滤出当前登录用户拥有权限的纪录
        """
        queryset = super(TaskListView, self).get_queryset()
        projects = get_objects_for_user(self.request.user, 'asset.view_projectproxymodel')

        if projects:
            new_queryset = queryset.filter(project__in=projects)
        else:
            new_queryset = []

        return new_queryset

    @method_decorator(login_required)
    @method_decorator(permission_required('code_update.add_taskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(TaskListView, self).dispatch(*args, **kwargs)
