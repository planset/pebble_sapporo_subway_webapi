# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=10)),
                ('name', models.CharField(default=b'', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('name_for_pebble', models.CharField(default=b'', max_length=255)),
                ('description', models.TextField(default=b'')),
                ('lat', models.FloatField(default=0)),
                ('lng', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StationDeparture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(default=b'', max_length=4)),
                ('holiday', models.BooleanField(default=False)),
                ('direction', models.CharField(default=b'fukuzumi', max_length=30)),
                ('station', models.ForeignKey(related_name=b'departures', to='station.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
