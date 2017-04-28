# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 00:10
from __future__ import unicode_literals

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('completed', models.BooleanField(default=False, help_text='This will be set to true once the reminder has been sent.')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.CreateModel(
            name='PrivateEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Event')),
                ('title', models.CharField(help_text='Give the event a title', max_length=100)),
                ('descriptionField', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('locationString', models.CharField(blank=True, help_text='If this event is not at a public event location, then enter it here.', max_length=200, null=True, verbose_name='Other Location')),
                ('link', models.URLField(blank=True, help_text='Optionally include the URL to anything that may be relevant for this event.')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.event',),
        ),
        migrations.CreateModel(
            name='PrivateEventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Category name will be displayed.', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Add an optional description.', null=True)),
                ('displayColor', colorfield.fields.ColorField(default='#0000FF', help_text='Choose a color for the calendar display.', max_length=10)),
                ('requiredGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Group required to add events to this category.')),
            ],
            options={
                'verbose_name_plural': 'Private events categories',
                'verbose_name': 'Private events category',
            },
        ),
        migrations.AddField(
            model_name='privateevent',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='private_events.PrivateEventCategory'),
        ),
        migrations.AddField(
            model_name='privateevent',
            name='displayToGroup',
            field=models.ForeignKey(blank=True, help_text='If this is set, then only these users will see this event on their calendar.', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Display to group'),
        ),
        migrations.AddField(
            model_name='privateevent',
            name='displayToUsers',
            field=models.ManyToManyField(blank=True, help_text='If this is set, then only chosen users will see this event on their calendar.', to=settings.AUTH_USER_MODEL, verbose_name='Display to users'),
        ),
        migrations.AddField(
            model_name='eventreminder',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Event'),
        ),
        migrations.AddField(
            model_name='eventreminder',
            name='eventOccurrence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.EventOccurrence', verbose_name='Event Occurrence'),
        ),
        migrations.AddField(
            model_name='eventreminder',
            name='notifyList',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Notification List'),
        ),
    ]
