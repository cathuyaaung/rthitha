# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rthitha.zmovies.models import Movie
from rthitha.tvseries.models import TVShow

def home(request):
	#return HttpResponse("Rango says hello world!")

    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    movie_list = Movie.objects.all().order_by("-created","-id")[:4]
    tvseries_list = TVShow.objects.all()

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'movie_list': movie_list, 'tvseries_list': tvseries_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('home.html', context_dict, context)