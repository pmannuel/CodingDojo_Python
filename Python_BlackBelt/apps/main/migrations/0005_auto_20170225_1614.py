# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170224_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joins',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips_joined', to='main.Trips'),
        ),
    ]
