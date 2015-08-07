from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views
 
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^cart/$', views.cart, name='cart'),
 url(r'^addcart/(?P<num>\d+)$', views.add_to_cart, name='add_to_cart'),
 url(r'^removecart/(?P<num>\d+)$', views.remove_from_cart, name='remove_from_cart'),
 url(r'^checkout/$', views.check_out, name='check_out'),
 url(r'^signup/$', views.signup, name='signup'),
 url(r'^register/$', views.register, name='register'),
 url(r'^login/$', views.login, name='login'),
 url(r'^login_user/$', views.login_user, name='login_user'),
 url(r'^my_account/$', views.my_account, name='my_account'),
 url(r'^logout/$', views.logout, name='logout'),
 url(r'^(?P<num>\d+)/$', views.product, name='product'),
 ]