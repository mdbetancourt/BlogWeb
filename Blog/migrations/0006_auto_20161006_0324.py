# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-06 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20161006_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Fecha de publicación'),
        ),
    ]
