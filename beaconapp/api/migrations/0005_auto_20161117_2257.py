# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_foundbeacon_lostbeacon'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='lostbeacon',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
