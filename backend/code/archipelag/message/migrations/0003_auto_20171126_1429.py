# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20171105_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagetype',
            name='service',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Prasa', 'Informacja Prasowa'), ('Newsletter', 'Newsletter'), ('Instagram', 'Instagram'), ('Twitter', 'Twitter'), ('SMS', 'SMS Kiss')], default='Facebook', max_length=10),
        ),
    ]
