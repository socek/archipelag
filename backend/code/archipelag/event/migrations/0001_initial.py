# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ngo', '0003_ngouser_fb_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120)),
                ('url', models.URLField(null=True)),
                ('date_starting', models.DateField()),
                ('date_ending', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('shares', models.PositiveIntegerField()),
                ('text', models.TextField(blank=True, max_length=2048)),
                ('hashtag', models.CharField(default='', max_length=128)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo.NgoUser')),
            ],
        ),
    ]
