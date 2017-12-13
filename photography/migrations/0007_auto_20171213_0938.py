# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-13 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0006_auto_20171212_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='thumb',
            field=imagekit.models.fields.ProcessedImageField(upload_to='MediaRootS3BotoStorage'),
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='height',
            field=models.IntegerField(default=1200),
        ),
        migrations.AlterField(
            model_name='albumimage',
            name='width',
            field=models.IntegerField(default=1920),
        ),
    ]
