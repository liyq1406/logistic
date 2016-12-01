from django.db import models
from container.models import Container,Car
from worker.models import Partment,Worker
from . import STATUS
# Create your models here.


class Mission(models.Model):
    car = models.ForeignKey(Car,verbose_name="执行车")
    worker = models.ManyToManyField(Worker,verbose_name="押运工作人员")
    added = models.DateTimeField('发布时间',auto_now_add = True)
    time_start = models.DateTimeField('开始时间')
    time_end = models.DateTimeField('结束时间')
    def __str__(self):
        return "{}由{}执行".format(self.time_start,self.car)
    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'


class Task(models.Model):
    origin = models.ForeignKey(Partment,verbose_name="起点")
    target = models.ForeignKey(Partment,verbose_name="目标点",related_name="ending")
    container = models.ManyToManyField(Container,verbose_name="货箱")
    misson = models.ForeignKey(Mission,verbose_name="任务")
    modified = models.DateTimeField('状态改变时间')
    status = models.CharField('状态',choices=STATUS,max_length=10)
    order = models.SmallIntegerField('顺序', default=0)
    def __str__(self):
        return "由{}送向{}".format(self.origin,self.target)
    class Meta:
        verbose_name = '任务节点'
        verbose_name_plural = '任务节点'

# class modifiedTask(models.Model):
#     added = models.DateTimeField('添加时间',auto_now_add=True)
#     banker = models.ForeignKey(Worker,verbose_name='银行验收员')
#     taskTime = models.DateTimeField('任务时间')
#     container = models.ManyToManyField(Container,verbose_name="货箱")
#     def __str__(self):
#         return "{}-{}".format(self.taskTime,self.banker.partment)
#     class Meta:
#         verbose_name = '更改任务节点'
#         verbose_name_plural = '更改任务节点'






