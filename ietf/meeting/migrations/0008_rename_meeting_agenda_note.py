# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0007_auto_20180716_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='agenda_note',
            new_name='agenda_warning_note',
        ),
    ]