# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from zmovies.models import Movie
from tvseries.models import TVShow
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from zmovies.models import UserProfile

def home(request):
	context = RequestContext(request)
	movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]
	tvseries_list = TVShow.objects.filter(active=True)

	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''

	context_dict = {
					'movie_list': movie_list, 
					'tvseries_list': tvseries_list,
					'userProfile':userProfile,
					}
	return render_to_response('home.html', context_dict, context)

def custom_404(request):
	return render_to_response('404.html')

def custom_500(request):
	return render_to_response('500.html')

def logout(request):
	"""Logs out user"""
	auth_logout(request)
	return HttpResponseRedirect(request.GET.get('next', '/'))

def loginerror(request):
	"""Login Error"""	
	return HttpResponseRedirect(request.GET.get('next', '/'))


def test(request,movie_title_url):
	context = RequestContext(request)
	movie = Movie.objects.get(id=movie_title_url)		
	movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]		
	print 'request.user',request.user
	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except:
		userProfile = ''

	context_dict = {'movie':movie, 'movie_list':movie_list, 'userProfile':userProfile}
	response = render_to_response('test.html', context_dict, context)
	return response