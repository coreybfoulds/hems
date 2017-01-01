from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	"""A blog topic"""
	text=models.TextField(max_length=100000)
	title=models.CharField(max_length=120)
	video=models.TextField(max_length=10000)
	image = models.FileField(null=True, blank=True)
	date_added=models.DateTimeField(auto_now=False, auto_now_add=True)
	def __unicode__(self):
		return self.text[:10000]




class Entry(models.Model):
	"""Blog entry"""
	topic=models.ForeignKey(Topic)
	owner=models.ForeignKey(User)
	text=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name_plural='entries'
	def __unicode__(self):
		return self.text[:51]+"..."
