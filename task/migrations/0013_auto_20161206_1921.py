# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-06 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0012_remove_task_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='worker.Partment', verbose_name='起始点'),
        ),
    ]