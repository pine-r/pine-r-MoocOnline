# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-22 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20190321_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u6570'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='students',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570'),
        ),
    ]
