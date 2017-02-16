from __future__ import unicode_literals

from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
