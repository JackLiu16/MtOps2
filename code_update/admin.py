from django.contrib import admin

from models import ProjectProxyModel, TaskModel

from guardian.admin import GuardedModelAdmin


class ProjectProxyAdmin(GuardedModelAdmin):
    pass

admin.site.register(ProjectProxyModel, ProjectProxyAdmin)

admin.site.register(TaskModel)
