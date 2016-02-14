# -*- coding:utf8 -*-
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext, ugettext_lazy as _
from utils.about_pwd import check_pw_strong


class UserPwdUpdateForm(PasswordChangeForm):
    """
    继承自 Django auth 中的表单，重写 old_password、new_password1、new_password2，
    为其增加样式类以及一些项目中所需的 HTML 属性。实现 clean_new_password1 方法用
    于密码强度检查。
    """
    error_messages = dict(PasswordChangeForm.error_messages, **{
        'password_strong': u'密码必须包涵大小写字母以及数字，并且不得少于8位。',
    })

    old_password = forms.CharField(label=_("Old password"),
        widget=forms.PasswordInput(attrs = {'class': 'form-control'})
    )
    new_password1 = forms.CharField(label=_("New password"),
        widget=forms.PasswordInput(attrs = {'class': 'form-control'})
    )
    new_password2 = forms.CharField(label=_("New password confirmation"),
        widget=forms.PasswordInput(attrs = {'class': 'form-control'})
    )

    def clean_new_password1(self):
        """
        密码强度检查
        """
        password1 = self.cleaned_data.get('new_password1')
        if not check_pw_strong(password1):
            raise forms.ValidationError(self.error_messages['password_strong'])
        return password1
