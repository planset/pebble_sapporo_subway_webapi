# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Station'
        db.create_table(u'station_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_for_pebble', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('lat', self.gf('django.db.models.fields.FloatField')()),
            ('lng', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'station', ['Station'])

        # Adding model 'StationDeparture'
        db.create_table(u'station_stationdeparture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('holiday', self.gf('django.db.models.fields.BooleanField')()),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['station.Station'])),
        ))
        db.send_create_signal(u'station', ['StationDeparture'])


    def backwards(self, orm):
        # Deleting model 'Station'
        db.delete_table(u'station_station')

        # Deleting model 'StationDeparture'
        db.delete_table(u'station_stationdeparture')


    models = {
        u'station.station': {
            'Meta': {'object_name': 'Station'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lng': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_for_pebble': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'station.stationdeparture': {
            'Meta': {'object_name': 'StationDeparture'},
            'holiday': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['station.Station']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['station']