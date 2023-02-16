from django.db import models
from user.models import User

class Routine(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="제목",max_length=30, unique=True)
    category_choice = (
        ('MIRACLE', 'MIRACLE'),
        ('HOMEWORK', 'HOMEWORK')
    )
    category = models.CharField(verbose_name="카테고리",max_length=15, choices=category_choice)
    goal = models.CharField(verbose_name="목표",max_length=40)
    is_alarm = models.BooleanField(verbose_name="알람여부",max_length=15)
    is_deleted = models.BooleanField(verbose_name="삭제여부",max_length=10, default=False)
    created_at = models.DateTimeField(verbose_name="생성시간",auto_now_add = True)
    modified_at = models.DateTimeField(verbose_name="수정시간",auto_now = True)
