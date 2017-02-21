from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="courses_index"),
    url(r'^courses/add$', views.add_course, name="courses_add"),
    url(r'^courses/destroy/(?P<course_id>\d+)$', views.rem_course, name="courses_del"),
]
