# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TVShow.poster'
        db.add_column('tvseries_tvshow', 'poster',
                      self.gf('django.db.models.fields.files.ImageField')(default='poster/None/no-img.jpg', max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TVShow.poster'
        db.delete_column('tvseries_tvshow', 'poster')


    models = {
        'tvseries.episode': {
            'Meta': {'object_name': 'Episode'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tvseries.Season']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'tvseries.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tvshow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tvseries.TVShow']"})
        },
        'tvseries.tvshow': {
            'Meta': {'object_name': 'TVShow'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'default': "'poster/None/no-img.jpg'", 'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['tvseries']