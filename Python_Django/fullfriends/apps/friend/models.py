from __future__ import unicode_literals

from django.db import models

class friend(models.Model):
    name=models.CharField(max_length=45)
    create_at=models.DateTimeField(auto_now_add=True)

class friendship(models.Model):
    friend2=models.ForeignKey(friend)
    friend1=models.ForeignKey(friend, related_name='friend1_in_ship')
