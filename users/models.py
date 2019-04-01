from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField('姓名', max_length=50,)
    mobile = models.CharField('手机号码', max_length=11, blank=True)
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

