# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-20 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180120_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(blank=True, default='\u65e5\u8bb0', null=True, to='blog.Tag', verbose_name='\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='link',
            name='link_des',
            field=models.CharField(blank=True, max_length=54, null=True, verbose_name='\u94fe\u63a5\u63cf\u8ff0'),
        ),
    ]
