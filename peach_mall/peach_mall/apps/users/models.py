from django.db import models
# 导入用于扩展用户表的类
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")

    class Meta:
        # 自定义表名，不使用默认生成的表名
        db_table = "tb_users"
        # 设置用户模型对象的直观、可读的名称
        verbose_name = "用户"
        # 复数形式，默认为"用户s"，一般设置为与verbose_name同名
        verbose_name_plural = verbose_name
