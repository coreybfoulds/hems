# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 18:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hems_blog', '0013_auto_20161110_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]