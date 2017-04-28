# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 00:10
from __future__ import unicode_literals

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
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', djangocms_text_ckeditor.fields.HTMLField(help_text='Answer the question.')),
                ('orderNum', models.PositiveIntegerField(default=0, help_text='This number specifies the order in which the questions will be shown on the FAQ page.')),
                ('draft', models.BooleanField(default=False, help_text='Check this box to prevent publication.')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('orderNum',),
            },
        ),
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('orderNum', models.PositiveIntegerField(default=0, help_text='This number specifies the order in which categories will be shown.')),
            ],
            options={
                'verbose_name_plural': 'FAQ Categories',
                'ordering': ('orderNum',),
            },
        ),
        migrations.CreateModel(
            name='FAQCategoryPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='faq_faqcategorypluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('showTitle', models.BooleanField(default=False, verbose_name='Show Category Title')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faq.FAQCategory')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='FAQSinglePluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='faq_faqsinglepluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faq.FAQ')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='faq',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faq.FAQCategory'),
        ),
    ]
