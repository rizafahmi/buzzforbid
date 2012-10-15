# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Hotel.address'
        db.delete_column('hotel_hotel', 'address')

        # Adding field 'Hotel.address1'
        db.add_column('hotel_hotel', 'address1',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=200),
                      keep_default=False)

        # Adding field 'Hotel.address2'
        db.add_column('hotel_hotel', 'address2',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Hotel.province'
        db.add_column('hotel_hotel', 'province',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hotel_province', null=True, to=orm['province.Province']),
                      keep_default=False)

        # Adding field 'Hotel.zipcode'
        db.add_column('hotel_hotel', 'zipcode',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Hotel.country'
        db.add_column('hotel_hotel', 'country',
                      self.gf('django.db.models.fields.CharField')(default='Indonesia', max_length=50),
                      keep_default=False)

        # Adding M2M table for field facilities on 'Hotel'
        db.create_table('hotel_hotel_facilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('hotel', models.ForeignKey(orm['hotel.hotel'], null=False)),
            ('facility', models.ForeignKey(orm['hotel_facility.facility'], null=False))
        ))
        db.create_unique('hotel_hotel_facilities', ['hotel_id', 'facility_id'])

    def backwards(self, orm):
        # Adding field 'Hotel.address'
        db.add_column('hotel_hotel', 'address',
                      self.gf('django.db.models.fields.TextField')(default=' '),
                      keep_default=False)

        # Deleting field 'Hotel.address1'
        db.delete_column('hotel_hotel', 'address1')

        # Deleting field 'Hotel.address2'
        db.delete_column('hotel_hotel', 'address2')

        # Deleting field 'Hotel.province'
        db.delete_column('hotel_hotel', 'province_id')

        # Deleting field 'Hotel.zipcode'
        db.delete_column('hotel_hotel', 'zipcode')

        # Deleting field 'Hotel.country'
        db.delete_column('hotel_hotel', 'country')

        # Removing M2M table for field facilities on 'Hotel'
        db.delete_table('hotel_hotel_facilities')

    models = {
        'city.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hotel.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_city'", 'to': "orm['city.City']"}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Indonesia'", 'max_length': '50'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'hotel_facility'", 'symmetrical': 'False', 'to': "orm['hotel_facility.Facility']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotel_province'", 'null': 'True', 'to': "orm['province.Province']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotel_region'", 'null': 'True', 'to': "orm['region.Region']"}),
            'room_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'hotel_facility.facility': {
            'Meta': {'object_name': 'Facility'},
            'facility': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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