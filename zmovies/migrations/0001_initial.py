# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table('zmovies_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('zmovies', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table('zmovies_movie')


    models = {
        'zmovies.movie': {
            'Meta': {'object_name': 'Movie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['zmovies']