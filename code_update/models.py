# -*- coding:utf8 -*-
from django.db import models

from django.db.models import Q

from django.contrib.auth.models import User

from asset.models import ProjectModel

from django.dispatch import receiver

from django.db.models.signals import post_save

from guardian.shortcuts import get_objects_for_user


class ProjectProxyModel(ProjectModel):
    """
    asset 应用 Project 模型代理
    """
    class Meta:
        proxy = True
        permissions = (
            ("view_projectproxymodel", "Can see available project"),
        )
        verbose_name = u'软件项目代理模型'
        verbose_name_plural = u'软件项目代理模型'


class ProjectExtModel(models.Model):
    """
    为 asset 资产应用 ProjectModel 扩展
    以下字段
    """
    project = models.OneToOneField(ProjectModel, verbose_name=u'绑定项目', db_column='project')
    run_script = models.CharField(verbose_name=u'上线脚本', db_column='run_script', max_length=30, default=u'未绑定')

    def __unicode__(self):
        return self.run_script

    class Meta:
        db_table = 'code_projectext'
        verbose_name = u'软件项目扩展属性'
        verbose_name_plural = u'软件项目扩展属性'


class TaskModel(models.Model):
    """
    上线任务模型
    """
    _SCHEDULE = (
                 ('0', u'待上线'),
#                 ('1', u'审核通过'),
#                 ('2', u'审核未通过'),
                 ('3', u'版本更新'),
                 ('4', u'版本回滚'),
                 ('5', u'查看上线变动'),
                )
    _STATUS = (
               ('0', u'任务进行中...'),
               ('1', u'任务 DONE'),
              )

    user = models.ForeignKey(User, verbose_name=u"代码上线责任人", db_column='user')
    project = models.ForeignKey(ProjectProxyModel, verbose_name=u"上线项目", db_column='project')
    code_version = models.CharField(verbose_name=u"项目版本号", db_column='code_version', max_length=100, default='master')
    put_date = models.DateTimeField(verbose_name=u"任务提交时间", db_column='put_date', auto_now_add=True)
    yw_user = models.CharField(verbose_name=u"运维责任人", db_column='yw_user', max_length=100, default='-')
    schedule = models.CharField(verbose_name=u"上线进度", db_column='schedule', choices= _SCHEDULE, max_length=1, default='0')
    status = models.CharField(verbose_name=u"任务状态", db_column='status', choices=_STATUS, max_length=1, default='0')
    script_output_log = models.TextField(verbose_name=u"上线脚本执行输出", db_column='script_output_log',
                                         default='==================== *下屏显示后台脚本执行输出* ====================\n',
                                        )
    update_count = models.IntegerField(verbose_name=u"更新操作次数", db_column='update_count', default='0')
    rollback_count = models.IntegerField(verbose_name=u"回滚操作次数", db_column='rollback_count', default='0')
    remark = models.CharField(verbose_name=u"备注信息", db_column='remark', max_length=50, help_text=u"如果需要可提交 50 字符长度的备注信息",
                              default='-'
                             )

    def __unicode__(self):
        return self.project.project_name

    def save(self, *args, **kwargs):
        """
        重写 save 方法，添加操作计数
        """
        if self.schedule == '3':
            self.update_count += 1
        elif self.schedule == '4':
            self.rollback_count += 1
        super(TaskModel, self).save(*args, **kwargs)

    class Meta:
        db_table = 'code_task'
        verbose_name = u'代码上线任务'
        verbose_name_plural = u'代码上线任务'


@receiver(post_save, sender=ProjectModel) # 绑定 Django 内建 post_save 信号
def project_ext_create(sender, instance, created, **kwargs):
    if created: # 判断信号事件是否为创建新纪录
        regproject = ProjectExtModel(project=instance)
        regproject.save()
