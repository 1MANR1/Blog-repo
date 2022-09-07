from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
	"""A blog model."""
	title = models.CharField(max_length=200)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Retrun a title and text represention of the model."""
		return f"{self.title}: {self.text[:50]}..."

