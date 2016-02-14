# -*- coding:utf8 -*-
from __future__ import absolute_import
from celery import shared_task
import commands

from .models import TaskModel

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@shared_task
def code_task(run_script, mod_name, action, code_version, task_id):
    """
    Celery 队列任务，代码上线下
    """
    run_script = '/www/ReleaseCode/{run_script} -m {mod_name} -t {task_id} -a {action} -v {code_version}'.format(run_script=run_script, mod_name=mod_name, task_id=task_id, action=action, code_version=code_version)
    result = commands.getstatusoutput(run_script)
    task = TaskModel.objects.get(pk=task_id)
    task.script_output_log += result[1]

    task.save(update_fields=['script_output_log']) # 默认情况下 Model save() 更新所有字段，通过传递 update_fields 参数改变这一行为，
                                                        # 只更新指定的字段，带来一些轻微的性能提升。
