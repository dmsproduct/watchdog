# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161103_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitor',
            old_name='cCategory',
            new_name='Category',
        ),
    ]
