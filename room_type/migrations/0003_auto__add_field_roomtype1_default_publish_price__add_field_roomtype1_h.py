# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RoomType1.default_publish_price'
        db.add_column('room_type_roomtype1', 'default_publish_price',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'RoomType1.high_season_publish_price'
        db.add_column('room_type_roomtype1', 'high_season_publish_price',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RoomType1.low_season_publish_price'
        db.add_column('room_type_roomtype1', 'low_season_publish_price',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'RoomType1.special_occation_publish_price'
        db.add_column('room_type_roomtype1', 'special_occation_publish_price',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'RoomType1.default_publish_price'
        db.delete_column('room_type_roomtype1', 'default_publish_price')

        # Deleting field 'RoomType1.high_season_publish_price'
        db.delete_column('room_type_roomtype1', 'high_season_publish_price')

        # Deleting field 'RoomType1.low_season_publish_price'
        db.delete_column('room_type_roomtype1', 'low_season_publish_price')

        # Deleting field 'RoomType1.special_occation_publish_price'
        db.delete_column('room_type_roomtype1', 'special_occation_publish_price')

    models = {
        'room_type.roomfacility': {
            'Meta': {'object_name': 'RoomFacility'},
            'facility': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'room_type.roomtype1': {
            'Meta': {'object_name': 'RoomType1'},
            'allotment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bed_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'default_price': ('django.db.models.fields.IntegerField', [], {}),
            'default_publish_price': ('django.db.models.fields.IntegerField', [], {}),
            'high_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_publish_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_publish_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_bed': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'room_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'room1_facility'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['room_type.RoomFacility']"}),
            'room_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'room_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_publish_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'room_type.roomtype2': {
            'Meta': {'object_name': 'RoomType2'},
            'allotment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bed_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'default_price': ('django.db.models.fields.IntegerField', [], {}),
            'high_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_bed': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'room_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'room2_facility'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['room_type.RoomFacility']"}),
            'room_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'room_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'room_type.roomtype3': {
            'Meta': {'object_name': 'RoomType3'},
            'allotment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bed_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'default_price': ('django.db.models.fields.IntegerField', [], {}),
            'high_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_bed': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'room_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'room3_facility'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['room_type.RoomFacility']"}),
            'room_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'room_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'room_type.roomtype4': {
            'Meta': {'object_name': 'RoomType4'},
            'allotment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bed_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'default_price': ('django.db.models.fields.IntegerField', [], {}),
            'high_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_bed': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'room_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'room4_facility'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['room_type.RoomFacility']"}),
            'room_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'room_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['room_type']