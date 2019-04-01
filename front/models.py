from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class Start(models.Model):
    S_CHOICES = (
        ('ys', '阳山'),
        ('qy', '清远'),
        ('gz', '广州'),
    )
    E_CHOICES = (
        ('ys', '阳山'),
        ('qy', '清远'),
        ('gz', '广州'),
    )
    start_choices = models.CharField('出发地点', max_length=20, choices=S_CHOICES, default='ys')
    end_choices = models.CharField('到达地点', max_length=20, choices=E_CHOICES,default='ys')
    name = models.CharField('车型+可载人数', max_length=20, blank=True)
    start_img = models.ImageField('图片', upload_to='images/%m%d', max_length=100, default='images/1.gif', blank=True)
    start_time = models.DateTimeField('出发时间')
    beizhu =models.CharField('备注', max_length=100, blank=True, null=True)



    class Meta:
        verbose_name = '测试'
        verbose_name_plural = '测试'
