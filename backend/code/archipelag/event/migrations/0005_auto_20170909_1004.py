# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_auto_20170909_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ngo.NgoUser'),
        ),
    ]