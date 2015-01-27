# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=30)),
                ('name_indo', models.CharField(max_length=50)),
                ('name_viet', models.CharField(max_length=50)),
                ('spec', models.CharField(max_length=20)),
                ('sale_price', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('sales_intro', models.TextField()),
                ('sales_intro_indo', models.TextField()),
                ('sales_intro_viet', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now_add=True, auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=10)),
                ('name_indo', models.CharField(max_length=20)),
                ('name_viet', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now_add=True, auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modify_time', models.DateTimeField(auto_now_add=True, auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='app.ProductCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='uom',
            field=models.ForeignKey(to='app.UOM'),
            preserve_default=True,
        ),
    ]
