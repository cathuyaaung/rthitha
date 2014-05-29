from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'movies.views.home', name='home'))