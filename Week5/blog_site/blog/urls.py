from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^(?P<num>\d+)/$', views.blog_id, name='blog_id'),
 url(r'^create/$', views.create, name='create'),
 ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)