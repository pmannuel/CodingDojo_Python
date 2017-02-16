from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/add$', views.add_course),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.rem_course),
]
