from django.contrib import admin

from .models import Project, Detail

# 在管理员页面展示项目和详情数据
admin.site.register(Project)
admin.site.register(Detail)