from django.db import models

# Create your models here.

class TVShow(models.Model):
	name = models.CharField(max_length=500)
	description = models.TextField()
	poster = models.ImageField(upload_to = 'poster/', default = 'poster/None/no-img.jpg', 
		null=True)

	def __unicode__(self):
		return '%s' % (self.name)

class Season(models.Model):
	tvshow = models.ForeignKey(TVShow)
	number = models.IntegerField(default=1)

	def __unicode__(self):
		return '%s - S%s' % (self.tvshow.name, self.number)	

class Episode(models.Model):
	season = models.ForeignKey(Season)
	number = models.IntegerField(default=1)
	title = models.CharField(max_length=500)
	description = models.TextField()
	location = models.CharField(max_length=500, null=True)

	def __unicode__(self):
		return '%s - S%s - E%s - %s' % \
				(self.season.tvshow.name, self.season.number, self.number, self.title )	