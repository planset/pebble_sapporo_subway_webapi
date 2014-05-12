# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Holiday.date'
        db.alter_column(u'station_holiday', 'date', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Holiday.date'
        db.alter_column(u'station_holiday', 'date', self.gf('django.db.models.fields.DateField')())

    models = {
        u'station.holiday': {
            'Meta': {'object_name': 'Holiday'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'station.station': {
            'Meta': {'object_name': 'Station'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'lng': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name_for_pebble': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'station.stationdeparture': {
            'Meta': {'object_name': 'StationDeparture'},
            'direction': ('django.db.models.fields.CharField', [], {'default': "'fukuzumi'", 'max_length': '30'}),
            'holiday': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'departures'", 'to': u"orm['station.Station']"}),
            'time': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4'})
        }
    }

    complete_apps = ['station']