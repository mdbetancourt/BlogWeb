# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-24 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Blog', '0014_auto_20161030_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación'),
        ),
        migrations.AlterField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación'),
        ),
    ]
