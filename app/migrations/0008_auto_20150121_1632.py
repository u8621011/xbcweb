# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150119_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name_indo',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='name_viet',
            field=models.CharField(blank=True, max_length=100),
            preserve_default=True,
        ),
    ]
