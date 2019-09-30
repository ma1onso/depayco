# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-11 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depayco', '0005_auto_20181011_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscription',
            name='canceled_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
