from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^trip_info/(?P<trip_id>\d+)$', views.trip_info, name='trip_info'),
    url(r'^join/(?P<trip_id>\d+)$', views.join, name='join'),
]
