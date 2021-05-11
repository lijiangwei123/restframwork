from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    description = models.TextField(verbose_name='描述')
    completed = models.BooleanField(verbose_name='是否完成', default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title