from django.db import models
import datetime

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=500)
	
	poster = models.ImageField(upload_to = 'poster/', default = 'poster/None/no-img.jpg',
		null=True)
	description = models.TextField(null=True, blank=True)
	year = models.CharField(max_length=10, null=True, blank=True)
	genre = models.CharField(max_length=500, null=True, blank=True)
	director = models.CharField(max_length=500, null=True, blank=True)
	writer = models.CharField(max_length=500, null=True, blank=True)
	stars = models.CharField(max_length=500, null=True, blank=True)
	imdburl = models.CharField(max_length=500, null=True, blank=True)
	imdbrating = models.CharField(max_length=500, null=True, blank=True)
	rottentomatorating = models.CharField(max_length=500, null=True, blank=True)
	tomatourl = models.CharField(max_length=500, null=True, blank=True)

	created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
	modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

	location = models.CharField(max_length=500)
	location2 = models.CharField(max_length=500, null=True, blank=True)
	location3 = models.CharField(max_length=500, null=True, blank=True)
	location4 = models.CharField(max_length=500, null=True, blank=True)
	location5 = models.CharField(max_length=500, null=True, blank=True)
	location6 = models.CharField(max_length=500, null=True, blank=True)
	location7 = models.CharField(max_length=500, null=True, blank=True)
	location8 = models.CharField(max_length=500, null=True, blank=True)
	location9 = models.CharField(max_length=500, null=True, blank=True)
	location10 = models.CharField(max_length=500, null=True, blank=True)

	subtitles1 = models.CharField(max_length=500, null=True, blank=True)
	subtitles2 = models.CharField(max_length=500, null=True, blank=True)


	active = models.BooleanField(default=True)

	def __unicode__(self):
		if self.active==True:
			return '%s' % (self.title,)
		else:
			return '%s [INACTIVE]' % (self.title,)




from django.contrib.auth.models import User    

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to = 'avatar/', default = 'poster/None/no-img.jpg',
		null=True)
	loginfrom = models.CharField(max_length=500, null=True, blank=True)
	profileurl = models.CharField(max_length=500, null=True, blank=True)

	def __unicode__(self):
		return '%s' % (self.user.username,)