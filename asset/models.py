# -*- coding:utf8 -*-
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save


class ProjectModel(models.Model):
    """
    软件项目模型
    """
    project_name = models.CharField(verbose_name=u'项目名称', db_column='project_name', max_length=50)
    project_alias = models.CharField(verbose_name=u'项目别名', db_column='project_alias', max_length=50,
                                     default='alias'
                                    )
    remark = models.TextField(verbose_name=u"备注", db_column='remark', help_text=u'项目描述')
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)

    def __unicode__(self):
        return self.project_name

    class Meta:
        db_table = 'asset_project'
        verbose_name = u'软件项目'
        verbose_name_plural = u'软件项目'


class IdcModel(models.Model):
    """
    机房模型
    """
    _LINK_TYPE = (
        ('0', u'联通'),
        ('1', u'电信'),
        ('2', u'教育网'),
        ('3', u'小运营商'),
        ('4', u'BGP'),
    )

    _POWER_TYPE = (
        ('0', u'交流电'),
        ('1', u'直流电'),
    )

    _IDC_STATUS = (
        ('0', u'在线'),
        ('1', u'下线'),
        ('2', u'测试'),
    )

    name = models.CharField(verbose_name=u'机房名称', db_column='name', max_length=50)
    address = models.CharField(verbose_name=u"机房地址" , db_column='address', max_length=128)
    contacts = models.CharField(verbose_name=u'机房联系人', db_column='contacts', max_length=50)
    phone = models.CharField(verbose_name=u'联系人电话', db_column='phone', max_length=50)
    link_type = models.CharField(verbose_name=u'链路类型', db_column='link_type', max_length=1, choices=_LINK_TYPE, default=0)
    bandwidth = models.FloatField(verbose_name=u'带宽／Gbps', db_column='bandwidth')
    cabinet_total = models.IntegerField(verbose_name=u'机柜数量', db_column='cabinet_tota')
    power_type = models.CharField(verbose_name=u'电源类型', db_column='power_type', max_length=1, choices=_POWER_TYPE)
    idc_status = models.CharField(verbose_name=u'机房状态', db_column='idc_status', max_length=1, choices=_IDC_STATUS)
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)
    remark = models.TextField(verbose_name=u'备注', db_column='remark')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'asset_idc'
        verbose_name = u'机房'
        verbose_name_plural = u'机房'


class CabinetModel(models.Model):
    """
    机柜模型
    """
    _STANDBY_POWER = (
        ('0', u'支持'),
        ('1', u'不支持'),
    )
    name = models.CharField(verbose_name=u'机柜名称', db_column='name', max_length=50)
    idc = models.ForeignKey(IdcModel, verbose_name=u"所属机房", db_column='idc')
    standby_power = models.CharField(verbose_name=u'是否双路电', db_column='standby_power', max_length=1, choices=_STANDBY_POWER)
    u = models.IntegerField(verbose_name=u'机柜u 数', db_column='u', default=42)
    voltage = models.IntegerField(verbose_name=u'供电电压／V', db_column='voltage')
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)
    remark = models.TextField(verbose_name=u'备注', db_column='remark')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'asset_cabinet'
        verbose_name = u'机柜'
        verbose_name_plural = u'机柜'


class HardwareModel(models.Model):
    """
    主机硬件配置
    """
    _NETWORK_CARD_RATE = (
        ('0', u'百兆'),
        ('1', u'千兆'),
        ('2', u'万兆'),
    )
    _DRAC = (
        ('0', u'支持'),
        ('1', u'不支持'),
    )
    _STANDBY_POWER = (
        ('0', u'支持'),
        ('1', u'不支持'),
    )

    model = models.CharField(verbose_name=u'型号', db_column='model', max_length=50)
    cpu = models.CharField(verbose_name=u'cpu 型号', db_column='cpu', max_length=50)
    cpu_total = models.IntegerField(verbose_name=u'cpu 个数', db_column='cpu_total')
    memory = models.FloatField(verbose_name=u'内存／G', db_column='memory')
    disk_type = models.CharField(verbose_name=u'硬盘类型', db_column='disk_type', max_length=50)
    disk_total = models.IntegerField(verbose_name=u'硬盘个数', db_column='disk_total')
    storage = models.IntegerField(verbose_name=u'存储容量／G', db_column='storage')
    network_card_total = models.IntegerField(verbose_name=u'网卡个数', db_column='network_card_total', default=1)
    network_card_rate = models.CharField(verbose_name=u'网卡速率', db_column='network_card_rate', max_length=1, choices=_NETWORK_CARD_RATE, default=0)
    drac = models.CharField(verbose_name=u'远程管理支持', db_column='drac', max_length=1, choices=_DRAC)
    standby_power = models.CharField(verbose_name=u'双电支持', db_column='standby_power', max_length=1, choices=_STANDBY_POWER, default=0)
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)
    remark = models.TextField(verbose_name=u'备注', db_column='remark', blank=True)

    def __unicode__(self):
        return self.model

    class Meta:
        db_table = 'asset_hardware'
        verbose_name = u'主机配置'
        verbose_name_plural = u'主机配置'


class HostModel(models.Model):
    """
    主机模型
    """
    _STATUS = (
        ('0', u'在线'),
        ('1', u'空闲'),
        ('2', u'报废'),
    )

    host_name = models.CharField(verbose_name=u'主机名', db_column='name', max_length=50, blank=True)
    sn = models.CharField(verbose_name=u'sn 服务码', db_column='sn', max_length=50)
    hardware = models.ForeignKey(HardwareModel, related_name='hardware_host',verbose_name=u"硬件配置", db_column='hardware')
    cabinet = models.ForeignKey(CabinetModel, related_name='cabinet_host', verbose_name=u"所属机柜", db_column='cabinet')
    os = models.CharField(verbose_name=u'操作系统', db_column='os', max_length=50)
    ip1 = models.GenericIPAddressField(verbose_name=u'网卡 1 ip 地址', db_column='ip1', blank=True, null=True)
    ip2 = models.GenericIPAddressField(verbose_name=u'网卡 2 ip 地址', db_column='ip2', blank=True, null=True)
    ip3 = models.GenericIPAddressField(verbose_name=u'网卡 3 ip 地址', db_column='ip3', blank=True, null=True)
    ip4 = models.GenericIPAddressField(verbose_name=u'网卡 4 ip 地址', db_column='ip4', blank=True, null=True)
    mac1 = models.CharField(verbose_name=u'网卡 1 mac 地址', db_column='mac1', max_length=50, blank=True)
    mac2 = models.CharField(verbose_name=u'网卡 2 mac 地址', db_column='mac2', max_length=50, blank=True)
    mac3 = models.CharField(verbose_name=u'网卡 3 mac 地址', db_column='mac3', max_length=50, blank=True)
    mac4 = models.CharField(verbose_name=u'网卡 4 mac 地址', db_column='mac4', max_length=50, blank=True)
    status = models.CharField(verbose_name=u'主机状态', db_column='status', max_length=1, choices=_STATUS)
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)
    remark = models.TextField(verbose_name=u'备注', db_column='remark', blank=True)

    def __unicode__(self):
        return self.host_name

    class Meta:
        db_table = 'asset_host'
        verbose_name = u'主机'
        verbose_name_plural = u'主机'


class HostHistoryModel(models.Model):
    """
    主机历史记录
    """
    host = models.ForeignKey(HostModel, verbose_name=u"主机", db_column='host')
    history = models.CharField(verbose_name=u'历史记录', db_column='history', max_length=100)
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)

    def __unicode__(self):
        return self.host.host_name

    class Meta:
        db_table = 'asset_host_history'
        verbose_name = u'主机历史记录'
        verbose_name_plural = u'主机历史记录'


@receiver(post_save, sender=HostModel)
def host_history(sender, instance, created, **kwargs):
    if created:
        history = u'%s %s 被创建' %(instance.host_name, instance.put_date.strftime('%Y-%m-%d %H:%M:%S'))
        history = HostHistoryModel(host=instance, history=history)
        history.save()
