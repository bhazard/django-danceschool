# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-20 21:46
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateeventcategory',
            name='displayColor',
            field=colorful.fields.RGBColorField(default='#0000FF', help_text='Choose a color for the calendar display.'),
        ),
    ]
