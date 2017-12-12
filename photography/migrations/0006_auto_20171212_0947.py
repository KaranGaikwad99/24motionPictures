# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-12 09:47
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0005_auto_20171201_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='MediaRootS3BotoStorage'),
        ),
    ]
