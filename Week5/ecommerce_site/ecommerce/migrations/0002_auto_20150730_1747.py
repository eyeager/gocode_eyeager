# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_first', models.CharField(max_length=30)),
                ('name_last', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=50)),
                ('credit_card', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='quatity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(to='ecommerce.State'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, to='ecommerce.Customer'),
            preserve_default=False,
        ),
    ]
