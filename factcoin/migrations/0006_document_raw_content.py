# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-17 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factcoin', '0005_connection_rating_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='raw_content',
            field=models.TextField(null=True, verbose_name='content'),
        ),
    ]
