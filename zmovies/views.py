# Create your views here.
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from zmovies.models import Movie, UserProfile

def home(request):
	context = RequestContext(request)

	try:
		movie_list = Movie.objects.filter(active=True).order_by("-created","-id")
	except Movie.DoesNotExist:
		raise Http404

	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''

	context_dict = {'movie_list': movie_list, 'userProfile':userProfile}
	
	return render_to_response('movielist.html', context_dict, context)

def moviedetail(request, movie_title_url):
	print 'request.user',request.user
	context = RequestContext(request)
	try:
		movie = Movie.objects.get(id=movie_title_url)		
		movie_list = Movie.objects.filter(active=True).order_by("-created","-id")[:4]				
	except:
		raise Http404
	
	userProfile = ''
	try:
		userProfile = UserProfile.objects.get(user=request.user.id)
		print 'userProfile',userProfile
		print 'userProfile.avatar',userProfile.avatar
	except UserProfile.DoesNotExist:
		print 'UserProfile DOES NOT EXIST request.user',request.user
		userProfile = ''	

	context_dict = {'movie':movie, 'movie_list':movie_list, 'userProfile':userProfile}
	response = render_to_response('moviedetail.html', context_dict, context)
	return response	
