from django.conf.urls import url, include
from . import views
from views import Posts, Welcome

urlpatterns = [
	url(r'^$', Welcome.as_view(), name='welcome'),
    url(r'^posts/$', Posts.as_view(), name='posts')
]
