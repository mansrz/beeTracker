# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='checkPoint',
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='latitude',
            field=models.FloatField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='longitude',
            field=models.FloatField(max_length=17, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='device',
            name='checkPoint',
            field=models.ManyToManyField(related_name='CheckPoints', null=True, to='tracker.CheckPoint', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='campo1',
            field=models.TextField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='campo2',
            field=models.TextField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='campo3',
            field=models.TextField(max_length=25, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='description',
            field=models.TextField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.TextField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='latitude',
            field=models.FloatField(max_length=17),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='longitude',
            field=models.FloatField(max_length=17),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='position',
            name='speed',
            field=models.TextField(max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
    ]
