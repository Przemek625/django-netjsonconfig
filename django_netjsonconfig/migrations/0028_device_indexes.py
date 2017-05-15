# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0027_simplify_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='model',
            field=models.CharField(blank=True, db_index=True, help_text='device model and manufacturer', max_length=64),
        ),
        migrations.AlterField(
            model_name='device',
            name='os',
            field=models.CharField(blank=True, db_index=True, help_text='operating system identifier', max_length=128, verbose_name='operating system'),
        ),
    ]
