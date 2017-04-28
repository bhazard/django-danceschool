# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 00:10
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('financial', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNumber', models.CharField(max_length=100, unique=True, verbose_name='Internal Invoice Number')),
                ('paypalInvoiceID', models.CharField(max_length=100, unique=True, verbose_name='Paypal Invoice ID')),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('paymentDate', models.DateTimeField(blank=True, null=True)),
                ('invoiceURL', models.URLField(blank=True, null=True, verbose_name='Invoice View URL')),
                ('payerViewURL', models.URLField(blank=True, null=True, verbose_name='Invoice Payment URL')),
                ('totalAmount', models.FloatField(verbose_name='Invoice Total Amount (net of discounts)')),
                ('itemList', models.TextField(blank=True, null=True, verbose_name='Item List Passed to Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='IPNCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceName', models.CharField(blank=True, max_length=100, null=True, verbose_name='Invoice Item Name')),
                ('invoiceNumber', models.CharField(max_length=50, verbose_name='Invoice Item Number')),
                ('mc_gross', models.FloatField(default=0, verbose_name='Gross Amount')),
                ('refundAmount', models.FloatField(default=0, verbose_name='Allocated Refund Amount')),
            ],
            options={
                'verbose_name': 'Paypal IPN Cart Item',
            },
        ),
        migrations.CreateModel(
            name='IPNMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('invoice', models.CharField(max_length=80, verbose_name='Invoice number')),
                ('generated_invoice', models.CharField(blank=True, max_length=100, null=True, verbose_name='Paypal-generated invoice number')),
                ('mc_fee', models.FloatField()),
                ('mc_gross', models.FloatField()),
                ('payment_status', models.CharField(max_length=30)),
                ('payment_date', models.DateTimeField()),
                ('txn_id', models.CharField(max_length=30, unique=True)),
                ('txn_type', models.CharField(max_length=30)),
                ('custom', models.TextField()),
                ('mc_currency', models.CharField(max_length=30)),
                ('payer_email', models.EmailField(max_length=254)),
                ('receiver_email', models.EmailField(max_length=254)),
                ('payer_id', models.CharField(max_length=30)),
                ('finalRegistration', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Registration', verbose_name='Final Registration')),
                ('paypalInvoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paypal.Invoice', verbose_name='Paypal-Submitted Invoice')),
                ('priorTransaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subsequenttransactions', to='paypal.IPNMessage')),
                ('registration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TemporaryRegistration', verbose_name='Initial Temporary Registration')),
            ],
            options={
                'permissions': (('allocate_refunds', 'Can allocate Paypal refunds to individual registration items'),),
                'verbose_name': 'Paypal IPN message',
            },
        ),
        migrations.CreateModel(
            name='PayNowFormModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='paypal_paynowformmodel', serialize=False, to='cms.CMSPlugin')),
                ('defaultAmount', models.FloatField(default=0, help_text='The initial value for gift certificate forms.', verbose_name='Default amount')),
                ('cancellationPage', cms.models.fields.PageField(help_text='When the user returns to the site, send them to this page.', on_delete=django.db.models.deletion.CASCADE, related_name='cancellationPageFor', to='cms.Page', verbose_name='Cancellation Page')),
                ('successPage', cms.models.fields.PageField(help_text='When the user returns to the site after a successful transaction, send them to this page.', on_delete=django.db.models.deletion.CASCADE, related_name='successPageFor', to='cms.Page', verbose_name='Success Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='ipncartitem',
            name='ipn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paypal.IPNMessage'),
        ),
        migrations.AddField(
            model_name='ipncartitem',
            name='revenueItem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.RevenueItem'),
        ),
    ]
