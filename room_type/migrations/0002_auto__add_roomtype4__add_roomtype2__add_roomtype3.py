# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RoomType4'
        db.create_table('room_type_roomtype4', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('allotment', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('room_size', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('bed_size', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('number_of_bed', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('short_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default_price', self.gf('django.db.models.fields.IntegerField')()),
            ('high_season_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('high_season_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('high_season_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('low_season_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('low_season_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('low_season_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('special_occation_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('special_occation_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('special_occation_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('room_type', ['RoomType4'])

        # Adding M2M table for field room_facilities on 'RoomType4'
        db.create_table('room_type_roomtype4_room_facilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('roomtype4', models.ForeignKey(orm['room_type.roomtype4'], null=False)),
            ('roomfacility', models.ForeignKey(orm['room_type.roomfacility'], null=False))
        ))
        db.create_unique('room_type_roomtype4_room_facilities', ['roomtype4_id', 'roomfacility_id'])

        # Adding model 'RoomType2'
        db.create_table('room_type_roomtype2', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('allotment', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('room_size', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('bed_size', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('number_of_bed', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('short_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default_price', self.gf('django.db.models.fields.IntegerField')()),
            ('high_season_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('high_season_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('high_season_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('low_season_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('low_season_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('low_season_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('special_occation_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('special_occation_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('special_occation_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('room_type', ['RoomType2'])

        # Adding M2M table for field room_facilities on 'RoomType2'
        db.create_table('room_type_roomtype2_room_facilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('roomtype2', models.ForeignKey(orm['room_type.roomtype2'], null=False)),
            ('roomfacility', models.ForeignKey(orm['room_type.roomfacility'], null=False))
        ))
        db.create_unique('room_type_roomtype2_room_facilities', ['roomtype2_id', 'roomfacility_id'])

        # Adding model 'RoomType3'
        db.create_table('room_type_roomtype3', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('allotment', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('room_size', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('bed_size', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('number_of_bed', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('short_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('default_price', self.gf('django.db.models.fields.IntegerField')()),
            ('high_season_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('high_season_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('high_season_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('low_season_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('low_season_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('low_season_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('special_occation_from', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('special_occation_to', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('special_occation_price', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('room_type', ['RoomType3'])

        # Adding M2M table for field room_facilities on 'RoomType3'
        db.create_table('room_type_roomtype3_room_facilities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('roomtype3', models.ForeignKey(orm['room_type.roomtype3'], null=False)),
            ('roomfacility', models.ForeignKey(orm['room_type.roomfacility'], null=False))
        ))
        db.create_unique('room_type_roomtype3_room_facilities', ['roomtype3_id', 'roomfacility_id'])

    def backwards(self, orm):
        # Deleting model 'RoomType4'
        db.delete_table('room_type_roomtype4')

        # Removing M2M table for field room_facilities on 'RoomType4'
        db.delete_table('room_type_roomtype4_room_facilities')

        # Deleting model 'RoomType2'
        db.delete_table('room_type_roomtype2')

        # Removing M2M table for field room_facilities on 'RoomType2'
        db.delete_table('room_type_roomtype2_room_facilities')

        # Deleting model 'RoomType3'
        db.delete_table('room_type_roomtype3')

        # Removing M2M table for field room_facilities on 'RoomType3'
        db.delete_table('room_type_roomtype3_room_facilities')

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
            'high_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'high_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_season_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'low_season_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_bed': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'room_facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'room1_facility'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['room_type.RoomFacility']"}),
            'room_size': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'room_type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_from': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'special_occation_price': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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