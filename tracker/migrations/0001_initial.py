# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campo1', models.TextField(max_length=12)),
                ('campo2', models.TextField(max_length=12)),
                ('campo3', models.TextField(max_length=12)),
                ('picture', models.ImageField(default=b'checkPoint/anonymous.png', upload_to=b'checkPoint/%Y/%m/%d', null=True, verbose_name=b'Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=12, null=True, blank=True)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(max_length=25, null=True, blank=True)),
                ('version', models.TextField(max_length=12, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(default=b'devices/anonymous.png', upload_to=b'devices/%Y/%m/%d', null=True, verbose_name=b'Devices')),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.TextField(max_length=12)),
                ('longitude', models.TextField(max_length=12)),
                ('altitude', models.TextField(max_length=12, null=True, blank=True)),
                ('speed', models.TextField(max_length=12, null=True, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('checkPoint', models.ForeignKey(related_name='event', blank=True, to='tracker.CheckPoint', null=True)),
            ],
            options={
                'verbose_name': 'Ubicaci\xf3n',
                'verbose_name_plural': 'Ubicaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(default=b'users/anonymous.png', upload_to=b'users/%Y/%m/%d', null=True, verbose_name=b'Users')),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('devices', models.ManyToManyField(related_name='Devices', to='tracker.Device')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Supervisor',
                'verbose_name_plural': 'Supervisores',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='device',
            name='positions',
            field=models.ManyToManyField(related_name='Positions', null=True, to='tracker.Position', blank=True),
            preserve_default=True,
        ),
    ]
