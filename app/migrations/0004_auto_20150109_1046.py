# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150104_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sort_order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='show_it',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
