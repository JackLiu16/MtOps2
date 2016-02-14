# -*- coding:utf8 -*-
from django import forms

from models import ProjectModel, IdcModel, CabinetModel, HardwareModel, HostModel


class ProjectCreateForm(forms.ModelForm):
    """
    软件项目创建表单
    """
    class Meta:
        model = ProjectModel
        fields = [
                  'project_name', 'project_alias', 'remark',
                 ]
        widgets = {
                   'project_name': forms.TextInput(attrs={'class': 'form-control',}),
                   'project_alias': forms.TextInput(attrs={'class': 'form-control',}),
                   'remark': forms.Textarea(attrs={'class': 'form-control',}),
                  }


class IdcCreateForm(forms.ModelForm):
    """
    机房信息创建表单
    """
    class Meta:
        model = IdcModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'address': forms.TextInput(attrs={'class': 'form-control',}),
            'contacts': forms.TextInput(attrs={'class': 'form-control',}),
            'phone': forms.TextInput(attrs={'class': 'form-control',}),
            'link_type': forms.Select(attrs={'class': 'form-control',},),
            'bandwidth': forms.NumberInput(attrs={'class': 'form-control',}),
            'server_racks_total': forms.NumberInput(attrs={'class': 'form-control',}),
            'power_type': forms.Select(attrs={'class': 'form-control',},),
            'idc_status': forms.Select(attrs={'class': 'form-control',},),
            'remark': forms.Textarea(attrs={'class': 'form-control',}),
        }


class CabinetCreateForm(forms.ModelForm):
    """
    机柜信息创建表单
    """
    class Meta:
        model = CabinetModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'idc': forms.Select(attrs={'class': 'form-control',},),
            'standby_power': forms.Select(attrs={'class': 'form-control',},),
            'u': forms.NumberInput(attrs={'class': 'form-control',}),
            'voltage': forms.NumberInput(attrs={'class': 'form-control',}),
            'remark': forms.Textarea(attrs={'class': 'form-control',}),
        }


class HardwareCreateForm(forms.ModelForm):
    """
    硬件信息床架表单
    """
    class Meta:
        model = HardwareModel
        fields = '__all__'
        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control',}),
            'cpu': forms.TextInput(attrs={'class': 'form-control',}),
            'cpu_total': forms.NumberInput(attrs={'class': 'form-control',}),
            'memory': forms.NumberInput(attrs={'class': 'form-control',}),
            'disk_type': forms.TextInput(attrs={'class': 'form-control',}),
            'disk_total': forms.NumberInput(attrs={'class': 'form-control',}),
            'storage': forms.NumberInput(attrs={'class': 'form-control',}),
            'network_card_rate': forms.Select(attrs={'class': 'form-control',},),
            'network_card_total': forms.NumberInput(attrs={'class': 'form-control',}),
            'drac': forms.Select(attrs={'class': 'form-control',},),
            'standby_power': forms.Select(attrs={'class': 'form-control',},),
            'remark': forms.Textarea(attrs={'class': 'form-control',}),
        }


class HostCreateForm(forms.ModelForm):
    """
    主机信息创建表单
    """
    class Meta:
        model = HostModel
        fields = '__all__'
        widgets = {
            'host_name': forms.TextInput(attrs={'class': 'form-control',}),
            'sn': forms.TextInput(attrs={'class': 'form-control',}),
            'hardware': forms.Select(attrs={'class': 'form-control',},),
            'cabinet': forms.Select(attrs={'class': 'form-control',},),
            'os': forms.TextInput(attrs={'class': 'form-control',}),
            'ip1': forms.TextInput(attrs={'class': 'form-control',}),
            'ip2': forms.TextInput(attrs={'class': 'form-control',}),
            'ip3': forms.TextInput(attrs={'class': 'form-control',}),
            'ip4': forms.TextInput(attrs={'class': 'form-control',}),
            'mac1': forms.TextInput(attrs={'class': 'form-control',}),
            'mac2': forms.TextInput(attrs={'class': 'form-control',}),
            'mac3': forms.TextInput(attrs={'class': 'form-control',}),
            'mac4': forms.TextInput(attrs={'class': 'form-control',}),
            'status': forms.Select(attrs={'class': 'form-control',},),
            'remark': forms.Textarea(attrs={'class': 'form-control',}),
        }
