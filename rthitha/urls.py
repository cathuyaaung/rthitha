from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rthitha import views
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
	url(r'^logout/$', 'rthitha.views.logout'),
	url(r'^test/(?P<movie_title_url>\w+)/$', views.test, name='test'),
    # Examples:
    #url(r'^$', 'rthitha.views.home', name='home'),
    # url(r'^rthitha/', include('rthitha.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # home
	url(r'^$', views.home, name='home'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),		

    # /movies
	url(r'^(?i)movies/', include('rthitha.zmovies.urls')),

    # /tvseries
    url(r'^(?i)tvseries/', include('rthitha.tvseries.urls')),    

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
)

urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


urlpatterns += staticfiles_urlpatterns()

handler404 = views.custom_404
handler500 = views.custom_500