# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-19 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestlistname',
            name='notes',
            field=models.CharField(blank=True, help_text='These will be included on the list for reference.', max_length=200, null=True, verbose_name='Notes (optional)'),
        ),
    ]
