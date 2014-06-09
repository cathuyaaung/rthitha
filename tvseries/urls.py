from django.conf.urls import patterns, include, url
from tvseries import views

urlpatterns = patterns('',
	url(r'^$', views.tvserieslist, name='tvserieslist'),

	url(r'^(?P<tvshow_id_url>\w+)/$', \
		views.seasonlist, name='seasonlist'),	

	url(r'^(?P<tvshow_id_url>\w+)/(?P<season_id_url>\w+)/$', \
		views.episodelist, name='episodelist'),	

	url(r'^(?P<tvshow_id_url>\w+)/(?P<season_id_url>\w+)/(?P<episode_id_url>\w+)/$', \
		views.episodedetail, name='episodedetail'),		

	)


