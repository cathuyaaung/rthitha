from django.db import models

# Create your models here.

class TVShow(models.Model):
	name = models.CharField(max_length=500)
	description = models.TextField()
	poster = models.ImageField(upload_to = 'poster/', default = 'poster/None/no-img.jpg',
		null=True)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		if self.active==True:
			return '%s' % (self.name,)
		else:
			return '%s [INACTIVE]' % (self.name,)

class Season(models.Model):
	tvshow = models.ForeignKey(TVShow)
	number = models.IntegerField(default=1)

	active = models.BooleanField(default=True)

	def __unicode__(self):		
		if self.active==True:
			return '%s - S%s' % (self.tvshow.name, self.number)
		else:
			return '%s - S%s [INACTIVE]' % (self.tvshow.name, self.number)

class Episode(models.Model):
	season = models.ForeignKey(Season)
	number = models.IntegerField(default=1)
	title = models.CharField(max_length=500)
	description = models.TextField()
	location = models.CharField(max_length=500, null=True)
	location2 = models.CharField(max_length=500, null=True, blank=True)
	location3 = models.CharField(max_length=500, null=True, blank=True)

	subtitles1 = models.CharField(max_length=500, null=True, blank=True)
	subtitles2 = models.CharField(max_length=500, null=True, blank=True)

	active = models.BooleanField(default=True)

	def __unicode__(self):
		if self.active==True:
			return '%s - S%s - E%s - %s' % \
				(self.season.tvshow.name, self.season.number, self.number, self.title )
		else:
			return '%s - S%s - E%s - %s [INACTIVE]' % \
				(self.season.tvshow.name, self.season.number, self.number, self.title )

