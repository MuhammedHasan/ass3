# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageCourse', '0002_auto_20151221_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='office',
            new_name='office_details',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='details',
        ),
    ]