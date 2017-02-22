from __future__ import unicode_literals
from django.db import models
from ..logreg.models import Users, Validator

class Secrets(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.CharField(max_length=50)
    # author = models.CharField(max_length=255)

class Likes(models.Model):
    user_liked = models.ForeignKey(Users)
    liked_secrets = models.ForeignKey(Secrets, related_name='secret_liked')
