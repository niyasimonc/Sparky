# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-04-24 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import file_mngmnt.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, default=None, null=True, upload_to=file_mngmnt.models.get_file_path)),
                ('version', models.CharField(default=b'', max_length=100)),
                ('file_name', models.CharField(default=b'', max_length=100)),
                ('description', models.CharField(blank=True, default=b'', max_length=2000)),
            ],
        ),
    ]
