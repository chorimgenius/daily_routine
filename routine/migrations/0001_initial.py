# Generated by Django 4.1.7 on 2023-02-20 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='제목')),
                ('category', models.CharField(choices=[('MIRACLE', 'MIRACLE'), ('HOMEWORK', 'HOMEWORK')], max_length=15, verbose_name='카테고리')),
                ('goal', models.CharField(max_length=40, verbose_name='목표')),
                ('is_alarm', models.BooleanField(max_length=15, verbose_name='알람여부')),
                ('is_deleted', models.BooleanField(default=False, max_length=10, verbose_name='삭제여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('NOT', '안함'), ('TRY', '시도'), ('DONE', '완료')], max_length=15, verbose_name='결과')),
                ('is_deleted', models.BooleanField(default=False, max_length=10, verbose_name='삭제여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('rountine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(verbose_name='요일')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routine.routine')),
            ],
        ),
    ]
