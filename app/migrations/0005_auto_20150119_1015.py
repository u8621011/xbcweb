# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150109_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(unique=True, blank=True, max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='code',
            field=models.CharField(serialize=False, max_length=2, primary_key=True),
            preserve_default=True,
        ),
    ]
