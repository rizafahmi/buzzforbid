# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Province'
        db.create_table('geographic_info_province', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('geographic_info', ['Province'])

        # Adding model 'Country'
        db.create_table('geographic_info_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('shortname', self.gf('django.db.models.fields.CharField')(max_length=5, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal('geographic_info', ['Country'])

        # Adding model 'City'
        db.create_table('geographic_info_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='city_country', to=orm['geographic_info.Country'])),
        ))
        db.send_create_signal('geographic_info', ['City'])

        # Adding model 'Region'
        db.create_table('geographic_info_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='city_region', to=orm['geographic_info.City'])),
            ('region_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('geographic_info', ['Region'])

    def backwards(self, orm):
        # Deleting model 'Province'
        db.delete_table('geographic_info_province')

        # Deleting model 'Country'
        db.delete_table('geographic_info_country')

        # Deleting model 'City'
        db.delete_table('geographic_info_city')

        # Deleting model 'Region'
        db.delete_table('geographic_info_region')

    models = {
        'geographic_info.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'city_country'", 'to': "orm['geographic_info.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'geographic_info.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'geographic_info.province': {
            'Meta': {'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'geographic_info.region': {
            'Meta': {'object_name': 'Region'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'city_region'", 'to': "orm['geographic_info.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['geographic_info']