from __future__ import unicode_literals

from django.db import models
from ..courses.models import Courses
from ..logreg.models import Users

class User_Courses(models.Model):
    course_id = models.ForeignKey(Courses, related_name='course_e')
    user_id = models.ForeignKey(Users, related_name='user_e')
