# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='id_connected_object',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
