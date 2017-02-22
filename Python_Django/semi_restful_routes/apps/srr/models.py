from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=45)
