from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^addCourse$', views.addCourse, name="addCourse"),
	url(r'^checkDelete/(?P<id>\d+)$', views.checkDelete, name='checkDelete'),
	url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]
