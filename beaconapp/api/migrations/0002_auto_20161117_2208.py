# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 22:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beacons', to=settings.AUTH_USER_MODEL),
        ),
    ]
