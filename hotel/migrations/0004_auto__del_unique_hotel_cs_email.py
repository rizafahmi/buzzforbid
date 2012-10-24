# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Hotel', fields ['cs_email']
        db.delete_unique('hotel_hotel', ['cs_email'])

    def backwards(self, orm):
        # Adding unique constraint on 'Hotel', fields ['cs_email']
        db.create_unique('hotel_hotel', ['cs_email'])

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'geographic_info.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'geographic_info.province': {
            'Meta': {'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'geographic_info.region': {
            'Meta': {'object_name': 'Region'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geographic_info.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'hotel.facility': {
            'Meta': {'object_name': 'Facility'},
            'facility': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'hotel.hotel': {
            'Meta': {'object_name': 'Hotel'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hotel_city'", 'to': "orm['geographic_info.City']"}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Indonesia'", 'max_length': '35'}),
            'cs_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'facilities': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hotel_facility'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['hotel.Facility']"}),
            'fax_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'manager_user'", 'unique': 'True', 'null': 'True', 'to': "orm['user_level.Manager']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotel_province'", 'null': 'True', 'to': "orm['geographic_info.Province']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'receptionist': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'receptionist_user'", 'unique': 'True', 'to': "orm['user_level.Receptionist']"}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hotel_region'", 'null': 'True', 'to': "orm['geographic_info.Region']"}),
            'room_type_1': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'hotel_room_type_1'", 'unique': 'True', 'to': "orm['room_type.RoomType1']"}),
            'room_type_2': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'hotel_room_type_2'", 'unique': 'True', 'null': 'True', 'to': "orm['room_type.RoomType2']"}),
            'room_type_3': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'hotel_room_type_3'", 'unique': 'True', 'null': 'True', 'to': "orm['room_type.RoomType3']"}),
            'room_type_4': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'hotel_room_type_4'", 'unique': 'True', 'null': 'True', 'to': "orm['room_type.RoomType4']"}),
            'supervisor': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'supervisor_user'", 'unique': 'True', 'null': 'True', 'to': "orm['user_level.Supervisor']"}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'room_type.roomfacility': {
            'Meta': {'object_name': 'RoomFacility'},
            'facility': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
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
            'include_breakfast': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        },
        'user_level.manager': {
            'Meta': {'object_name': 'Manager'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'user_level.receptionist': {
            'Meta': {'object_name': 'Receptionist'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'user_level.supervisor': {
            'Meta': {'object_name': 'Supervisor'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['hotel']