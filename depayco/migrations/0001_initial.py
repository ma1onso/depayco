# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-09 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(help_text='Example: 9xRxhaJ2YmLTkT5uz', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('credit_card_token', models.CharField(help_text='Example: eXj5Wdqgj7xzvC7AR', max_length=20)),
                ('identification_type', models.CharField(choices=[('CC', 'Cédula de ciudadanía'), ('CE', 'Cédula de extranjería '), ('NIT', 'Número de Identificación Tributaria'), ('DNI', 'Documento nacional de identidad')], max_length=5)),
                ('identification_number', models.CharField(max_length=200)),
                ('delinquent', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.CharField(help_text='Example: unity_3d_course', max_length=30, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('currency', models.CharField(max_length=3)),
                ('interval', models.CharField(choices=[('day', 'Day'), ('week', 'Week'), ('month', 'Month'), ('year', 'Year')], max_length=5)),
                ('interval_count', models.IntegerField()),
                ('trial_days', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.CharField(help_text='Example: efPXtZ5r4nZRoPtjZ', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depayco.Customer')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depayco.Plan')),
            ],
        ),
    ]
