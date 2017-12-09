# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 14:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0002_auto_20171120_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='album',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 11, 27, 14, 33, 28, 16871, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='alt',
            field=models.CharField(default=uuid.uuid4, max_length=255),
        ),
    ]