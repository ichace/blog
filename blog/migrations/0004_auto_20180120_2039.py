# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-20 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180120_2023'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '\u53cb\u60c5\u94fe\u63a5', 'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': '\u7559\u8a00', 'verbose_name_plural': '\u7559\u8a00'},
        ),
    ]