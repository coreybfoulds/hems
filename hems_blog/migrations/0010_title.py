# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hems_blog', '0009_auto_20161109_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hems_blog.Topic')),
            ],
        ),
    ]
