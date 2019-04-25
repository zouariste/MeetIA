# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-24 02:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Reunion', '0002_auto_20190423_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pv',
            old_name='soumise',
            new_name='soumis',
        ),
        migrations.AddField(
            model_name='point',
            name='hasChanged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 4, 24, 2, 26, 27, 364000, tzinfo=utc), editable=False),
        ),
    ]
