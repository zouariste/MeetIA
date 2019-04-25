# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-23 19:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Reunion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pv',
            name='soumise',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reunion',
            name='soumise',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 23, 19, 13, 45, 409000, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='pv',
            name='file',
            field=models.FileField(null=True, upload_to='pv'),
        ),
    ]
