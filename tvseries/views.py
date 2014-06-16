# Create your views here.
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from tvseries.models import TVShow, Season, Episode
from zmovies.models import UserProfile


def tvserieslist(request):
	context = RequestContext(request)
	try:
		tvseries_list = TVShow.objects.filter(active=True)
	except TVShow.DoesNotExist:
		raise Http404

	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''

	context_dict = {
					'tvseries_list': tvseries_list,
					'userProfile':userProfile,
					}
	return render_to_response('tvserieslist.html', context_dict, context)



def seasonlist(request, tvshow_id_url):
	context = RequestContext(request)
	tvshow = TVShow.objects.get(id=tvshow_id_url)
	season_list = Season.objects.filter(tvshow=tvshow_id_url, active=True).order_by('number')

	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''

	context_dict = {
					'tvshow' : tvshow, 
					'season_list': season_list, 
					'userProfile':userProfile,
					}
	return render_to_response('tvseriesseasonlist.html', context_dict, context)

def episodelist(request, tvshow_id_url, season_id_url):
	context = RequestContext(request)
	tvshow = TVShow.objects.get(id=tvshow_id_url)
	season = Season.objects.get(id=season_id_url)
	episode_list = Episode.objects.filter(season=season_id_url, active=True).order_by('number')

	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''

	context_dict = {
					'tvshow' : tvshow, 
					'season' : season, 
					'episode_list': episode_list,
					'userProfile':userProfile,
					}
	return render_to_response('tvseriesepisodelist.html', context_dict, context)

def episodedetail(request, tvshow_id_url, season_id_url, episode_id_url):
	context = RequestContext(request)
	tvshow = TVShow.objects.get(id=tvshow_id_url)
	season = Season.objects.get(id=season_id_url)    
	episode = Episode.objects.get(id=episode_id_url)
	episode_list = Episode.objects.filter(season=season_id_url, active=True).order_by('number')
    
	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''

	context_dict = {
					'tvshow' : tvshow, 
					'season' : season, 
					'episode': episode, 
					'episode_list':episode_list,
					'userProfile':userProfile,
					}
	return render_to_response('tvseriesepisodedetail.html', context_dict, context)    

