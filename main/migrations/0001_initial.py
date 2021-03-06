# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_website', models.CharField(max_length=200)),
                ('company_logo', models.FileField(upload_to='')),
                ('company_notes', models.TextField(max_length=100000)),
                ('company_twitter', models.CharField(max_length=200)),
                ('company_facebook', models.CharField(max_length=200)),
                ('company_linkedin', models.CharField(max_length=200)),
                ('company_category', models.CharField(max_length=200)),
                ('company_crunchbase', models.CharField(max_length=200)),
                ('company_similarweb', models.CharField(max_length=200)),
            ],
        ),
    ]
