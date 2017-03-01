from django.conf.urls import url, include
from . import views
from views import add_note, delete_note

urlpatterns = [
	url(r'^$', views.index, name ="index"),
    url(r'^add_note$', add_note.as_view(), name ="add_note"),
    url(r'^edit$', views.edit, name ="edit"),
	url(r'^delete_note$', delete_note.as_view(), name="delete_note")
]
