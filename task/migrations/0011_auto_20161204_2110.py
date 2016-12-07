# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-04 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20161204_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='worker.Partment', verbose_name='起始点'),
        ),
        migrations.AlterField(
            model_name='task',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_place', to='worker.Partment', verbose_name='目标点'),
        ),
    ]
