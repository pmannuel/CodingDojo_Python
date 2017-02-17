from __future__ import unicode_literals

from django.db import models

import re

class EmailValidator(models.Manager):
      def register(self, email):
          EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

          if not EMAIL_REGEX.match(email) or len(email) < 1:
              flash = {
                  "isvalid" : False,
                  "message" : "Email is not Valid",
                  "txt_color" : "red"
              }
              return flash
          else:
              flash = {
                  "isvalid" : True,
                  "message" : "{} is a valid email address. Thank you!".format(email),
                  "txt_color" : "green"
              }
              return flash

class Users(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    validate = EmailValidator()
