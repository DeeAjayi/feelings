# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-02 15:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thought',
            name='recorded',
        ),
        migrations.AddField(
            model_name='thought',
            name='recorded_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 2, 15, 50, 30, 785026, tzinfo=utc), editable=False),
        ),
    ]
