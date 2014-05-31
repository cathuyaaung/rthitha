# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TVShow'
        db.create_table('tvseries_tvshow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('tvseries', ['TVShow'])

        # Adding model 'Season'
        db.create_table('tvseries_season', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tvshow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvseries.TVShow'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('tvseries', ['Season'])

        # Adding model 'Episode'
        db.create_table('tvseries_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvseries.Season'])),
            ('number', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
        ))
        db.send_create_signal('tvseries', ['Episode'])


    def backwards(self, orm):
        # Deleting model 'TVShow'
        db.delete_table('tvseries_tvshow')

        # Deleting model 'Season'
        db.delete_table('tvseries_season')

        # Deleting model 'Episode'
        db.delete_table('tvseries_episode')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['tvseries']