from .models import Project, Detail
from django.shortcuts import render


# 展示所有项目的后台逻辑
def index(request):
    # 从数据库中查找所有的项目
    project_list = Project.objects.all()
    # 渲染页面发送给前端
    context = {'project_list': project_list}
    return render(request, 'index.html', context)


# 展示项目详情的后台逻辑
def project(request, project_id):
    # 从数据库中查找指定项目
    the_project = Project.objects.get(id=project_id)
    # 查找出改项目的所有申请详情
    detail_list = the_project.detail_set.all()
    # 渲染页面发送给前端
    context = {'project': the_project, 'detail_list': detail_list}
    return render(request, 'project.html', context)