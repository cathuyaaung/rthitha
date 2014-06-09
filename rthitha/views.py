# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rthitha.zmovies.models import Movie
from rthitha.tvseries.models import TVShow
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
	context = RequestContext(request)
	movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]
	tvseries_list = TVShow.objects.filter(active=True)
	context_dict = {'movie_list': movie_list, 'tvseries_list': tvseries_list}
	return render_to_response('home.html', context_dict, context)

def custom_404(request):
	return render_to_response('404.html')

def custom_500(request):
	return render_to_response('500.html')

def logout(request):
	"""Logs out user"""
	auth_logout(request)
	context = RequestContext(request)
	movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]
	tvseries_list = TVShow.objects.filter(active=True)
	context_dict = {'movie_list': movie_list, 'tvseries_list': tvseries_list}
	#return render_to_response('home.html', context_dict, context)
	return HttpResponseRedirect(request.GET.get('next', '/'))

def test(request,movie_title_url):
	context = RequestContext(request)
	movie = Movie.objects.get(id=movie_title_url)		
	movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]		
	context_dict = {'movie':movie, 'movie_list':movie_list}
	response = render_to_response('test.html', context_dict, context)
	return response