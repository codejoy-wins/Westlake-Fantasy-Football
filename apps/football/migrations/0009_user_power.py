# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-12 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0008_player_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='power',
            field=models.IntegerField(default=0),
        ),
    ]