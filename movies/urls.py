from django.conf.urls import patterns, url
from rthitha import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))