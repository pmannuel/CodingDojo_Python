from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)$', views.index, name='index'),
    url(r'^edit_profile/(?P<user_id>\d+)$', views.edit_profile, name='edit_profile'),
]
