from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.google import GoogleOAuth2Backend
from social_auth.backends.twitter import TwitterBackend

from zmovies.models import UserProfile

import urllib

from django.conf import settings #or from my_project import settings


def get_user_avatar(backend, details, response, social_user, uid,\
					user, *args, **kwargs):
	print 'get user avatar'
	url = None
	if backend.__class__ == FacebookBackend:
		url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

	elif backend.__class__ == TwitterBackend:
		url = response.get('profile_image_url', '').replace('_normal', '')

	elif backend.__class__ == GoogleOAuth2Backend and "picture" in response:
		url = response["picture"]

	print url
	if url:
		destination = settings.MEDIA_ROOT + '/avatar/' + user.username + '.jpg'
		urllib.urlretrieve(url, destination)		
		print destination
		print 'file written'
		print user.id
		userid = user.id


		try:		
			userProfile = UserProfile.objects.get(user=user)
			print "exist"
		except:
			print "does not exist"
			userProfile = UserProfile(user=user)

		userProfile.avatar = 'avatar/' + user.username + '.jpg'
		userProfile.save()			