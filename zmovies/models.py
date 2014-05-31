from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=500)
	location = models.CharField(max_length=500)
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

	def __unicode__(self):
		return '%s' % self.title

