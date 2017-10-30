# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SECUREPAY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=500)),
                ('amount', models.CharField(max_length=500)),
                ('rmb_amount', models.CharField(max_length=500)),
                ('vendor', models.CharField(max_length=500)),
                ('reference', models.CharField(max_length=500)),
                ('ipn_url', models.CharField(max_length=500)),
                ('callback_url', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('note', models.CharField(max_length=500)),
                ('terminal', models.CharField(max_length=500)),
                ('timeout', models.CharField(max_length=500)),
            ],
        ),
    ]