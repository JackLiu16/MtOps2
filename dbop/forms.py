# -*- coding:utf8 -*-
from django import forms

from django.forms.formsets import BaseFormSet

from models import CTTaskModel, CTSqlModel

from django.utils.functional import cached_property

from utils.request_api import MtDbApi

from django.utils.translation import ugettext, ugettext_lazy as _

from django.core.exceptions import ValidationError


class CTTaskCreateForm(forms.ModelForm):
    """
    创建数据库普通建表任务
    """
    class Meta:
        model = CTTaskModel
        fields = ['task_title', 'db_name', 'host_ip', 'port', 'remark']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control',}),
            'db_name': forms.TextInput(attrs={'class': 'form-control',}),
            'host_ip': forms.TextInput(attrs={'class': 'form-control',}),
            'port': forms.NumberInput(attrs={'class': 'form-control',}),
            'remark': forms.Textarea(attrs={'class': 'form-control',}),
        }


class CTSqlCreateForm(forms.ModelForm):
    """
    创建数据库普通建表子任务
    """
    class Meta:
        model = CTSqlModel
        fields = ['ct_sql', 'core_sql', 'rw_io']
        widgets = {
            'ct_sql': forms.Textarea(attrs={'class': 'form-control'}),
            'core_sql':forms.Textarea(attrs={'class': 'form-control'}),
            'rw_io': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.host = kwargs.pop('host_ip', None)
        self.port = kwargs.pop('port', None)
        self.db_name = kwargs.pop('db_name', None)
        super(CTSqlCreateForm, self).__init__(*args, **kwargs)

    def clean_ct_sql(self):
        """
        前台 Ajax 跨域访问代理，请求 DB API 做 SQL 语法规范检查
        """
        dbapi_request = MtDbApi("autoddl/ddl_create_check")
        ct_sql = self.cleaned_data.get('ct_sql')

        result = dbapi_request.ct_check(host=self.host, port=self.port, db_name=self.db_name, sql=ct_sql)

       
        if result.has_key('exception'):
            raise forms.ValidationError(result.get('exception'))

        if result.get('status') != 0:
            errmsg = result.get('result').get("extra").get("errmsg")
            raise ValidationError([ValidationError(_(i)) for i in errmsg])

        return ct_sql

class CTSqlBaseFormSet(BaseFormSet):
    """
    为formset 中的form 增加额外值，django 1.9 中增加了form_kwargs 属性，
    由于项目目前使用的是django 1.8，所以继承BaseFormSet 重写相应的方法。
    """
    def __init__(self, *args, **kwargs):
        self.form_kwargs = kwargs.pop('form_kwargs', {})
        super(CTSqlBaseFormSet, self).__init__(*args, **kwargs)

    @cached_property
    def forms(self):
        """
        Instantiate forms at first property access.
        """
        forms = [self._construct_form(i, **self.get_form_kwargs(i))
                 for i in range(self.total_form_count())]
        return forms

    def get_form_kwargs(self, index):
        """
        Return additional keyword arguments for each individual formset form.
        index will be None if the form being constructed is a new empty
        form.
        """
        return self.form_kwargs.copy()
