from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_index'),
    url(r'^user_to_course$', views.add_user_to_course, name='user_to_course'),
]
