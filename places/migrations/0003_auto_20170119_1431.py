# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_web_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coordinates',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
