from __future__ import unicode_literals
from django.db import models
from ..logreg.models import Users, Validator

class Secrets(models.Model):
    user = models.ForeignKey(Users)
    content = models.CharField(max_length=255)
    isLiked = models.BooleanField(default=False)
    created_at = models.CharField(max_length=50)


class Likes(models.Model):
    user_liked = models.ForeignKey(Users, related_name='user_liking')
    liked_secrets = models.ForeignKey(Secrets, related_name='secret_liked')
