from django.conf.urls import url
from django.contrib import admin
from .views import create,delete,update,details,post_home


urlpatterns = [
    url(r'^$',post_home,name="home"),
    url(r'^(?P<id>\d+)/delete/$',delete),
    url(r'^create/$',create,name="create"),
    url(r'^(?P<slug>.+)/update/$',update,name="update"),
    url(r'^(?P<slug>.+)/$',details,name="post_details"),

]