from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# from common.models import Common

# Create your models here.


class Setting(models.Model):
    objects = None
    user = models.OneToOneField('common.Common',on_delete=models.CASCADE, verbose_name="사용자")
    weight = models.CharField(max_length=20, verbose_name="체중",)
    fat = models.CharField(max_length=20, verbose_name="체지방량",)
    muscle = models.CharField(max_length=20, verbose_name="골격근량")
    target_weight = models.CharField(max_length=20, verbose_name="목표체중",)


    class Meta:
        db_table = "UserSetting"
        verbose_name = "setting"