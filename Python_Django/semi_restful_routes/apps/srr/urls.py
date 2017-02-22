from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<product_id>\d+)$', views.show, name='show'),
    url(r'^edit/(?P<product_id>\d+)$', views.edit, name='edit'),
    url(r'^save_edit/(?P<product_id>\d+)$', views.save_edit, name='save_edit'),
    url(r'^remove/(?P<product_id>\d+)$', views.remove, name='remove'),
    url(r'^addprod$', views.addprod, name='addprod'),
]
