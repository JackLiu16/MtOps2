# -*- coding:utf8 -*-
from django import forms

from models import ProjectExtModel, TaskModel


class ProjectUpdateForm(forms.ModelForm):
    """
    项目注册表单
    """
    class Meta:
        model = ProjectExtModel
        fields = ['run_script']
        widgets = {
                   'run_script': forms.TextInput(attrs={'class': 'form-control',}),
                  }

class TaskCreateForm(forms.ModelForm):
    """
    上线任务创建表单
    """
    class Meta:
        model = TaskModel
        fields = ['project', 'code_version', 'remark']
        widgets = {
                   'project': forms.Select(attrs={'class': 'form-control',},),
                   'code_version': forms.TextInput(attrs={'class': 'form-control',}),
                   'remark': forms.TextInput(attrs={'class': 'form-control',}),
                  }


class TaskUpdateForm(forms.ModelForm):
    """
    上线任务更新表单
    """
    _SCHEDULE = (
        ('3', u'版本更新'),
        ('4', u'版本回滚'),
        ('5', u'查看上线变动'),
    )
    schedule = forms.CharField(label=u'上线进度', widget=forms.Select(choices=_SCHEDULE, attrs={'class': 'form-control',}))
    class Meta:
        model = TaskModel
        fields = ['schedule', 'status']
        widgets = {
                   'status': forms.Select(attrs={'class': 'form-control',},),
                  }
