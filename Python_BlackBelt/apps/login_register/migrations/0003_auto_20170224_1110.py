# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0002_auto_20170224_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='name',
            new_name='firstname',
        ),
    ]