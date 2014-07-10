# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Episode.location2'
        db.add_column(u'tvseries_episode', 'location2',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Episode.location3'
        db.add_column(u'tvseries_episode', 'location3',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Episode.subtitles1'
        db.add_column(u'tvseries_episode', 'subtitles1',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Episode.subtitles2'
        db.add_column(u'tvseries_episode', 'subtitles2',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Episode.location2'
        db.delete_column(u'tvseries_episode', 'location2')

        # Deleting field 'Episode.location3'
        db.delete_column(u'tvseries_episode', 'location3')

        # Deleting field 'Episode.subtitles1'
        db.delete_column(u'tvseries_episode', 'subtitles1')

        # Deleting field 'Episode.subtitles2'
        db.delete_column(u'tvseries_episode', 'subtitles2')


    models = {
        u'tvseries.episode': {
            'Meta': {'object_name': 'Episode'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'location2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'location3': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvseries.Season']"}),
            'subtitles1': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'subtitles2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'tvseries.season': {
            'Meta': {'object_name': 'Season'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tvshow': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvseries.TVShow']"})
        },
        u'tvseries.tvshow': {
            'Meta': {'object_name': 'TVShow'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'default': "'poster/None/no-img.jpg'", 'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['tvseries']