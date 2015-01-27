# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uom',
            name='name_indo',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='uom',
            name='name_viet',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='name_indo',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='name_viet',
            field=models.CharField(blank=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sales_intro',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sales_intro_indo',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sales_intro_viet',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='spec',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name_indo',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name_viet',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
    ]
