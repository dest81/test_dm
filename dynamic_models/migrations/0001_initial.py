# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'users'
        db.create_table('dynamic_models_users', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('paycheck', self.gf('django.db.models.fields.IntegerField')(max_length='255')),
            ('date_joined', self.gf('django.db.models.fields.DateField')(max_length='255')),
        ))
        db.send_create_signal('dynamic_models', ['users'])

        # Adding model 'rooms'
        db.create_table('dynamic_models_rooms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length='255')),
            ('spots', self.gf('django.db.models.fields.IntegerField')(max_length='255')),
        ))
        db.send_create_signal('dynamic_models', ['rooms'])


    def backwards(self, orm):
        # Deleting model 'users'
        db.delete_table('dynamic_models_users')

        # Deleting model 'rooms'
        db.delete_table('dynamic_models_rooms')


    models = {
        'dynamic_models.rooms': {
            'Meta': {'object_name': 'rooms'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spots': ('django.db.models.fields.IntegerField', [], {'max_length': "'255'"})
        },
        'dynamic_models.users': {
            'Meta': {'object_name': 'users'},
            'date_joined': ('django.db.models.fields.DateField', [], {'max_length': "'255'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'255'"}),
            'paycheck': ('django.db.models.fields.IntegerField', [], {'max_length': "'255'"})
        }
    }

    complete_apps = ['dynamic_models']