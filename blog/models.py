from django.db import models

# Create your models here.

from django.core.urlresolvers import reverse

class post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	puplish = models.DateTimeField(auto_now=False, auto_now_add=True)
	update = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def get_url(self):
		return reverse('detail', kwargs={'id':self.id})
