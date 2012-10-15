# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Facility'
        db.create_table('hotel_facility', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('hotel', ['Facility'])

    def backwards(self, orm):
        # Deleting model 'Facility'
        db.delete_table('hotel_facility')

    models = {
        'city.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hotel.facility': {
            'Meta': {'object_name': 'Facility'},
            'facility': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hotel.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_city'", 'to': "orm['city.City']"}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Indonesia'", 'max_length': '50'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'hotel_facility'", 'symmetrical': 'False', 'to': "orm['hotel.Facility']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotel_province'", 'null': 'True', 'to': "orm['province.Province']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotel_region'", 'null': 'True', 'to': "orm['region.Region']"}),
            'room_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'province.province': {
            'Meta': {'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'region.region': {
            'Meta': {'object_name': 'Region'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['city.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['hotel']