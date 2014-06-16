from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rthithasite import views
#from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'', include('social_auth.urls')),
	url(r'^logout/$', 'rthithasite.views.logout'),
	
	url(r'^test/(?P<movie_title_url>\w+)/$', views.test, name='test'),

	#url(r'^login-error/$', 'rthithasite.views.loginerror'),

    # home
	url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),		
	url(r'^(?i)movies/', include('zmovies.urls')),
    url(r'^(?i)tvseries/', include('tvseries.urls')),    

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),

 	(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))


urlpatterns += staticfiles_urlpatterns()

handler404 = views.custom_404
handler500 = views.custom_500