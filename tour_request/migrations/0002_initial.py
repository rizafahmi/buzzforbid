# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Request'
        db.create_table('tour_request_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('adult', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('child', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('airplane', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('accomodation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('special_request', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='request_user', to=orm['auth.User'])),
        ))
        db.send_create_signal('tour_request', ['Request'])

        # Adding M2M table for field destinations on 'Request'
        db.create_table('tour_request_request_destinations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('request', models.ForeignKey(orm['tour_request.request'], null=False)),
            ('city', models.ForeignKey(orm['geographic_info.city'], null=False))
        ))
        db.create_unique('tour_request_request_destinations', ['request_id', 'city_id'])

    def backwards(self, orm):
        # Deleting model 'Request'
        db.delete_table('tour_request_request')

        # Removing M2M table for field destinations on 'Request'
        db.delete_table('tour_request_request_destinations')

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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'city_country'", 'to': "orm['geographic_info.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'geographic_info.country': {
            'Meta': {'object_name': 'Country'},
            'country': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'tour_request.request': {
            'Meta': {'object_name': 'Request'},
            'accomodation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'adult': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'airplane': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'child': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'destinations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'destination'", 'symmetrical': 'False', 'to': "orm['geographic_info.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'special_request': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'request_user'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['tour_request']