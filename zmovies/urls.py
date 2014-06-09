from django.conf.urls import patterns, include, url
from zmovies import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),

	url(r'^(?P<movie_title_url>\w+)/$', views.moviedetail, name='moviedetail'),	

	)


