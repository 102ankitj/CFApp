# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakefactory', '0003_auto_20170329_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='related_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cakefactory.Order'),
            preserve_default=False,
        ),
    ]
