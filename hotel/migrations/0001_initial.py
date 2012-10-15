# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hotel'
        db.create_table('hotel_hotel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['city.City'])),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['region.Region'], null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('room_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('hotel', ['Hotel'])

    def backwards(self, orm):
        # Deleting model 'Hotel'
        db.delete_table('hotel_hotel')

    models = {
        'city.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hotel.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['city.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['region.Region']", 'null': 'True', 'blank': 'True'}),
            'room_type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'region.region': {
            'Meta': {'object_name': 'Region'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['city.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['hotel']