# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rthitha.tvseries.models import TVShow, Season, Episode


def tvserieslist(request):
    context = RequestContext(request)
    tvseries_list = TVShow.objects.all()
    context_dict = {'tvseries_list': tvseries_list}
    return render_to_response('tvserieslist.html', context_dict, context)

def seasonlist(request, tvshow_id_url):
    context = RequestContext(request)
    tvshow = TVShow.objects.get(id=tvshow_id_url)
    season_list = Season.objects.filter(tvshow=tvshow_id_url).order_by('number')
    context_dict = {'tvshow' : tvshow, 'season_list': season_list}
    return render_to_response('tvseriesseasonlist.html', context_dict, context)

def episodelist(request, tvshow_id_url, season_id_url):
    context = RequestContext(request)
    tvshow = TVShow.objects.get(id=tvshow_id_url)
    season = Season.objects.get(id=season_id_url)
    episode_list = Episode.objects.filter(season=season_id_url).order_by('number')
    context_dict = {'tvshow' : tvshow, 'season' : season, 'episode_list': episode_list}
    return render_to_response('tvseriesepisodelist.html', context_dict, context)

def episodedetail(request, tvshow_id_url, season_id_url, episode_id_url):
    context = RequestContext(request)
    tvshow = TVShow.objects.get(id=tvshow_id_url)
    season = Season.objects.get(id=season_id_url)    
    episode = Episode.objects.get(id=episode_id_url)
    context_dict = {'tvshow' : tvshow, 'season' : season, 'episode': episode}
    return render_to_response('tvseriesepisodedetail.html', context_dict, context)    

