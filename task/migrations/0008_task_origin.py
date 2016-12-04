# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-03 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_auto_20161127_1345'),
        ('task', '0007_mission_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_place', to='worker.Partment', verbose_name='起始点'),
        ),
    ]
