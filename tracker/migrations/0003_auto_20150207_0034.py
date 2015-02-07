# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20150122_0050'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkpoint',
            options={'verbose_name': 'CheckPoint', 'verbose_name_plural': 'CheckPoints'},
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 7, 0, 34, 9, 456480, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='latitude',
            field=models.FloatField(default=0.0, max_length=17),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='longitude',
            field=models.FloatField(default=0.0, max_length=17),
            preserve_default=True,
        ),
    ]
