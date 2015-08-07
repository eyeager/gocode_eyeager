from django.conf.urls import url
 
from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^blah/$', views.blah, name='blah'),
 url(r'^create/$', views.create, name='create'),
 url(r'^(?P<num>\d+)/$', views.lookup, name='lookup'),
 ]