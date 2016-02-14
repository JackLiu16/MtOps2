# -*- coding:utf8 -*-
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required

from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from models import CTTaskModel, CTSqlModel

from django.forms.formsets import formset_factory
from forms import CTTaskCreateForm, CTSqlCreateForm, CTSqlBaseFormSet


class CTTaskCreateView(CreateView):
     """
     创建普通建表任务全局信息
     """
     model = CTTaskModel
     form_class = CTTaskCreateForm
     template_name = 'dbop/main_cttask_create.html'
     success_url = reverse_lazy('dbop-ct_task-list')

     def form_valid(self, form):
         """
         为非用户提交字段在后台自动创建相应的值
         """
         form.instance.user = self.request.user
         return super(CTTaskCreateView, self).form_valid(form)

     @method_decorator(login_required)
     @method_decorator(permission_required('dbop.add_cttaskmodel', raise_exception=True))
     def dispatch(self, *args, **kwargs):
         return super(CTTaskCreateView, self).dispatch(*args, **kwargs)


class CTTaskUpdateView(UpdateView):
    """
    编辑普通建表任务
    """
    model = CTTaskModel
    pk_url_kwarg = 'ct_task_id'
    form_class = CTTaskCreateForm
    template_name = 'dbop/main_cttask_create.html'
    success_url = reverse_lazy('dbop-ct_task-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('dbop.change_cttaskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(CTTaskUpdateView, self).dispatch(*args, **kwargs)


class GetDeleteMixin(object):
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class CTTaskDeleteView(GetDeleteMixin, DeleteView):
    """
    删除任务
    """
    model = CTTaskModel
    pk_url_kwarg = 'ct_task_id'
    success_url = reverse_lazy('dbop-ct_task-list')

    @method_decorator(login_required)
    @method_decorator(permission_required('dbop.delete_cttaskmodel', raise_exception=True))
    def dispatch(self, *args, **kwargs):
        return super(CTTaskDeleteView, self).dispatch(*args, **kwargs)


#class CTTaskDetailView(DetailView):
#    """
#    普通建表任务详情页面
#    """
#    model = 


class CTTaskListView(ListView):
    """
    任务列表
    """
    model = CTTaskModel
    template_name = 'dbop/main_cttask_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CTTaskListView, self).dispatch(*args, **kwargs)


@login_required
@permission_required('dbop.add_ctsqlmodel', raise_exception=True)
def ct_sub_task_create(request, ct_task_id):
    """
    添加普通建表任务执行SQL
    """
    ct_task = CTTaskModel.objects.get(pk=ct_task_id)
    CTSqlCreateFormSet = formset_factory(CTSqlCreateForm, formset=CTSqlBaseFormSet,
        extra=4, min_num=1, max_num=5,
        validate_min=True, validate_max=True, can_delete=True,
    )

    if request.method == 'POST':
        formset = CTSqlCreateFormSet(request.POST, request.FILES,
            form_kwargs={'host_ip': ct_task.host_ip,'port': ct_task.port, 'db_name': ct_task.db_name}
        )

        if formset.is_valid():
           for form_cleaned_data in formset.cleaned_data:
               if not form_cleaned_data or form_cleaned_data.get('DELETE', False):
                   continue

               ct_sql = form_cleaned_data['ct_sql']
               rw_io = form_cleaned_data['rw_io']
               core_sql = form_cleaned_data['core_sql']

               ct_sql_info = CTSqlModel(ct_task=ct_task, ct_sql=ct_sql, rw_io=rw_io,
                   core_sql=core_sql
               )
               ct_sql_info.save()
           return HttpResponseRedirect(reverse('dbop-ctmaintask-list'))
    else:
        formset = CTSqlCreateFormSet()
    return render_to_response('dbop/sub_cttask_create.html', locals(), context_instance=RequestContext(request))
        

#@login_required
#def ajax_cors_agent(request):
#    """
#    用于解决前端 ajax 跨域请求，代理访问 db api
#    """
#    if request.method == "POST":
#        form = CTSubTaskCreateForm(
#            {"ct_sql": request.POST["ct_sql"]}, host_ip=request.POST["host_ip"],
#            port=request.POST["port"], db_name=request.POST["db_name"]
#        )
#        if form.is_valid():
#            return JsonResponse({'is_success': 'true'})
#        else:
#            errors = []
#            for k, v in form.errors.items():
#                errors = errors + v

#            return JsonResponse({'is_success': 'false', 'error_message': errors})
