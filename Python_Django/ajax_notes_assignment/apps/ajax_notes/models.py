from __future__ import unicode_literals
from django.db import models

class Notes(models.Model):
	title = models.TextField()
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
