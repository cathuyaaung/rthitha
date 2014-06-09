# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from zmovies.models import Movie


def home(request):
	context = RequestContext(request)
	movie_list = Movie.objects.filter(active=True).order_by("-created","-id")
	context_dict = {'movie_list': movie_list}
	return render_to_response('movielist.html', context_dict, context)

def moviedetail(request, movie_title_url):
	context = RequestContext(request)
	try:
		movie = Movie.objects.get(id=movie_title_url)		
		movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]		
		context_dict = {'movie':movie, 'movie_list':movie_list}
	except:
		raise Http404

	response = render_to_response('moviedetail.html', context_dict, context)
	return response	
