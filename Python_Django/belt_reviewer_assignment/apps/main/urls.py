from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<user_id>\d+)$', views.user, name='user'),
    url(r'^books/(?P<book_id>\d+)$', views.book, name='book'),
    url(r'^del_review/(?P<review_id>\d+)$', views.del_review, name='del_review'),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review, name='add_review'),
]
