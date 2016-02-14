# -*- coding:utf8 -*-
from django.db import models

from django.contrib.auth.models import User


class CTTaskModel(models.Model):
    """
    数据库普通建表主任务
    """
    SCHEDULE = (
        ('0', u'等待审核...'),
        ('1', u'审核通过'),
        ('2', u'审核未通过'),
        ('3', u'任务进行中'),
        ('4', u'子任务失败'),
        ('4', u'任务 DONE'),
    )
    task_title = models.CharField(verbose_name=u"任务标题", db_column='task_title', max_length=100)
    user = models.ForeignKey(User, verbose_name='任务责任人', db_column='user')
    dba_user = models.CharField(verbose_name=u"DBA 责任人", db_column='dba_user', max_length=100, default='-')
    db_name = models.CharField(verbose_name=u'数据库', db_column='db_name', max_length=100, help_text=u'待操作的数据库名称')
    host_ip = models.GenericIPAddressField(verbose_name=u'IP 地址', db_column='host_ip', help_text=u'数据库服务 IP 地址')
    port = models.IntegerField(verbose_name=u'端口', db_column='port', help_text=u'数据库服务监听端口')
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)
    remark = models.TextField(verbose_name=u'备注', db_column='remark', help_text=u'普通建表任务描述')
    schedule = models.CharField(verbose_name=u'任务进度', db_column='schedule', choices=SCHEDULE, default='0', max_length='1')

    def __unicode__(self):
        return self.host + ':' + self.port

    class Meta:
        db_table = 'dbop_ct_task'
        verbose_name = u'数据库普通建表任务'
        verbose_name_plural = u'数据库普通建表任务'


class CTSqlModel(models.Model):
    """
    数据库普通建表子任务
    """
    STATUS = (
        ('0', u'SQL 通过语法检查'),
        ('1', u'建表中'),
        ('2', u'建表完成'),
        ('3', u'建表失败'),
    )
    ct_task = models.ForeignKey(CTTaskModel, verbose_name=u'隶属主任务', db_column='main_task')
    ct_sql = models.TextField(verbose_name=u'任务 SQL', db_column='ct_sql', help_text=u'输入任务建表 SQL')
    rw_io = models.TextField(verbose_name=u'读写量', db_column='rw_io', help_text=u'数据库读写量预估')
    core_sql = models.TextField(verbose_name=u'核心 SQL', db_column='core_sql', help_text=u'核心 sql 语句')
    put_date = models.DateTimeField(verbose_name=u"记录添加时间", db_column='put_date', auto_now_add=True)
    status = models.CharField(verbose_name=u'任务状态', db_column='status', choices=STATUS, default='0', max_length='1')
    schedule = models.IntegerField(verbose_name=u'任务执行百分比', db_column='schedule', default=0)

    class Meta:
        db_table = 'dbop_ct_sql'
        verbose_name = u'数据库普通建表子任务'
        verbose_name_plural = u'数据库普通建表子任务'

    def __unicode__(self):
        return self.id
