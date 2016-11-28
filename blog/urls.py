"""

BLOG APP URLS

"""
from django.conf.urls import url
from .views import (
	post_list, 
	post_create, 
	post_delete, 
	post_update, 
	post_home, 
	post_detail,
	)

urlpatterns = [

	url(r'^$', post_list, name="list"),
	url(r'^create/$', post_create),
	url(r'^(?P<id>\d+)/delete/$', post_delete, name="delete"),
	url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
	url(r'^$', post_detail, name="detail"),
	url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
	url(r'^a/', post_create)

]
