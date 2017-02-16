from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.show_ninjas),
    url(r'^ninjas/(?P<color>\w+)$', views.show_the_ninja)
]
