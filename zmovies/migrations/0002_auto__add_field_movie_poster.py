# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.poster'
        db.add_column('zmovies_movie', 'poster',
                      self.gf('django.db.models.fields.files.ImageField')(default='poster/None/no-img.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.poster'
        db.delete_column('zmovies_movie', 'poster')


    models = {
        'zmovies.movie': {
            'Meta': {'object_name': 'Movie'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'default': "'poster/None/no-img.jpg'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['zmovies']