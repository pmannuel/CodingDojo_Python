from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logreg/register$', views.register, name='register'),
    url(r'^logreg/login$', views.login, name='login'),
]
