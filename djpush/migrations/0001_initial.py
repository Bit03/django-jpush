# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 11:55
from __future__ import unicode_literals

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
            name='JiGuangReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regid', models.CharField(max_length=24, verbose_name='RegID')),
                ('is_push', models.BooleanField(default=True, verbose_name='Is Push')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Ji Guang Reg id',
                'verbose_name_plural': 'Ji Guang Reg id',
            },
        ),
    ]
