# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170107_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]