from django.db import models


# 项目总表
class Project(models.Model):
    # 项目名称
    project_name = models.CharField(max_length=100)
    # 单位名称
    company_name = models.CharField(max_length=100)
    # 总额度
    total_budget = models.FloatField()

    def __str__(self):
        return str(self.project_name) + '，总额度：' + str(self.total_budget) + '，剩余额度：' + str(self.budget_left())

    # 剩余额度
    def budget_left(self):
        budget = 0.0
        # 查找出所有的不是FAILED状态的明细，累加起来，用总额度减去它
        for detail in self.detail_set.all():
            if detail.status != Detail.Status.FAILED.name:
                budget += detail.budget
        return self.total_budget - budget


# 明细表
class Detail(models.Model):
    # 所属的项目，如果项目有明细，则该项目不能被删除，需要删除所有该项目的明细才能删除项目。
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    # 申请金额
    budget = models.FloatField()

    class Status(models.TextChoices):
        NEW = 'NEW', '申请已提交，等待审核'
        INTERNAL_ACCEPT = 'INTERNAL_ACCEPT', '内部审核通过'
        THIRD_PARTY = 'THIRD_PARTY', '材料已发给第三方公司'
        SUCCESS = 'SUCCESS', '第三方公司金额已发放'
        FAILED = 'FAILED', '申请失败'
    # 申请的状态
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return str(self.project) + '，' + self.status_name() + '，申请金额：' + str(self.budget)

    def status_name(self):
        return Detail.Status[self.status].label