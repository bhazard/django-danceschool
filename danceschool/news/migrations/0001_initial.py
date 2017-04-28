# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 00:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNewsPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='news_latestnewspluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('maxItems', models.PositiveSmallIntegerField(default=1, verbose_name='Maximum number of items to show')),
                ('daysBefore', models.PositiveSmallIntegerField(blank=True, help_text='Leave blank for no limit.', null=True, verbose_name='Published since (days ago)')),
                ('alertOnly', models.BooleanField(default=False, verbose_name='Show Alerts Only')),
                ('ignorePins', models.BooleanField(default=False, help_text='By default, pinned items are shown first, regardless of publication date. Checking this box overrides that behavior.', verbose_name='Ignore Pinned Item Precedence')),
                ('template', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title the news item. Make sure this is descriptive.', max_length=200)),
                ('content', djangocms_text_ckeditor.fields.HTMLField(help_text='Insert news content here.')),
                ('alert', models.BooleanField(default=False, help_text='Alerts (such as cancellations) may be displayed in an emphasized fashion.')),
                ('pinThis', models.BooleanField(default=False, help_text='If this field is set, then the news item will continue to show up on the main page until someone unpins it.', verbose_name='Pinned')),
                ('draft', models.BooleanField(default=False, help_text='Check to hide from publication')),
                ('hideThis', models.BooleanField(default=False, help_text='If for some reason you need to make a news item invisible, this will do that.', verbose_name='Hidden')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True, help_text='Time of most recent edit')),
                ('publicationDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-pinThis', '-publicationDate'),
            },
        ),
    ]
