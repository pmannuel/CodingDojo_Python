# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joining_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_register.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=255)),
                ('travel_date_from', models.DateTimeField()),
                ('travel_date_to', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='login_register.Users')),
            ],
        ),
        migrations.AddField(
            model_name='joins',
            name='trips',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Trips'),
        ),
    ]