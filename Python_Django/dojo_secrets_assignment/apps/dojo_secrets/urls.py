from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addsecret$', views.addsecret, name='addsecret'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like'),
]
