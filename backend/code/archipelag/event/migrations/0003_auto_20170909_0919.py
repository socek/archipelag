# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20170909_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='shares',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
