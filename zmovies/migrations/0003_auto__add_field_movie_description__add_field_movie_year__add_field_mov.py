# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.description'
        db.add_column('zmovies_movie', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Movie.year'
        db.add_column('zmovies_movie', 'year',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True),
                      keep_default=False)

        # Adding field 'Movie.genre'
        db.add_column('zmovies_movie', 'genre',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Movie.director'
        db.add_column('zmovies_movie', 'director',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Movie.writer'
        db.add_column('zmovies_movie', 'writer',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Movie.stars'
        db.add_column('zmovies_movie', 'stars',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Movie.imdburl'
        db.add_column('zmovies_movie', 'imdburl',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Movie.imdbrating'
        db.add_column('zmovies_movie', 'imdbrating',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)

        # Adding field 'Movie.rottentomatorating'
        db.add_column('zmovies_movie', 'rottentomatorating',
                      self.gf('django.db.models.fields.CharField')(max_length=500, null=True),
                      keep_default=False)


        # Changing field 'Movie.poster'
        db.alter_column('zmovies_movie', 'poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting field 'Movie.description'
        db.delete_column('zmovies_movie', 'description')

        # Deleting field 'Movie.year'
        db.delete_column('zmovies_movie', 'year')

        # Deleting field 'Movie.genre'
        db.delete_column('zmovies_movie', 'genre')

        # Deleting field 'Movie.director'
        db.delete_column('zmovies_movie', 'director')

        # Deleting field 'Movie.writer'
        db.delete_column('zmovies_movie', 'writer')

        # Deleting field 'Movie.stars'
        db.delete_column('zmovies_movie', 'stars')

        # Deleting field 'Movie.imdburl'
        db.delete_column('zmovies_movie', 'imdburl')

        # Deleting field 'Movie.imdbrating'
        db.delete_column('zmovies_movie', 'imdbrating')

        # Deleting field 'Movie.rottentomatorating'
        db.delete_column('zmovies_movie', 'rottentomatorating')


        # Changing field 'Movie.poster'
        db.alter_column('zmovies_movie', 'poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        'zmovies.movie': {
            'Meta': {'object_name': 'Movie'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imdbrating': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'imdburl': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'default': "'poster/None/no-img.jpg'", 'max_length': '100', 'null': 'True'}),
            'rottentomatorating': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'stars': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'writer': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        }
    }

    complete_apps = ['zmovies']