# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150104_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='spec',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name_indo',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name_viet',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
